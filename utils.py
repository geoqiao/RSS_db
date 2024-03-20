from typing import Dict, List, Optional

import feedparser
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine(
    "sqlite:///subscriptions.db", connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    pass


class Subscription(Base):
    __tablename__ = "feeds"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    tag: Mapped[Optional[str]]
    link: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"Feed(id={self.id!r}, url={self.url!r},title={self.title},tag={self.tag!r},link={self.link!r})"


Base.metadata.create_all(bind=engine)


def add_feed_to_db(url: str, title: str, tag: str | None, link: str):
    feed = Feed(url=url)
    with Session(engine) as session:
        session.add(Subscription(url=url, title=feed.title, tag=tag, link=feed.link))
        session.commit()
        session.close()


def get_all_feeds():
    with Session(engine) as session:
        feeds = session.query(Subscription).all()
        return feeds


def get_feed_by_id(feed_id: int):
    with Session(engine) as session:
        feed = session.query(Subscription).filter(Subscription.id == feed_id).first()
        return feed


def get_articles_for_feed(feed_id: int):
    feed_db = get_feed_by_id(feed_id)
    feed = Feed(feed_db.url)
    articles = feed.articles()
    return articles


class Feed:
    def __init__(self, url: str, tag: str | None = None) -> None:
        self.feed_parse = feedparser.parse(url)
        self.title = self.feed_parse.feed.title
        self.link = self.feed_parse.feed.link
        self.rss_feed = url
        self.tag = tag

    def articles(self) -> List[Dict[str, str]]:
        """list all the articles of Feed"""
        articles = []
        for entry in self.feed_parse.entries:
            article = {"title": entry.title, "link": entry.link}
            articles.append(article)
        return articles

    def __str__(self) -> str:
        return f"{self.title} -> {self.link}"

    def __repr__(self) -> str:
        return f"Feed({self.title})"
