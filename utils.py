from typing import Dict, List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column,Session
import feedparser


engine = create_engine(
    "sqlite:///subscriptions.db", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


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


# class Subscription(Base):
#     __tablename__ = "subscriptions"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     url = Column(String, nullable=False, unique=True, index=True)
#     title = Column(String)
#     tag = Column(String)
#     link = Column(String, index=True)


Base.metadata.create_all(bind=engine)


def add_feed_to_db(url: str, title: str, tag: str | None,link:str):
    feed = Feed(url=url)
    with Session(engine) as session:
        session.add(Subscription(url=url, title=feed.title, tag=tag, link=feed.link))
        session.commit()
        session.close()

def get_all_feeds():
    with Session(engine) as session:
        feeds = session.query(Subscription).all()
        return feeds

print(get_all_feeds())

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
