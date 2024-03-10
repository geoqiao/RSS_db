from typing import Dict, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import feedparser
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from fastapi import Depends


engine = create_engine(
    "sqlite:///subscriptions.db", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False, unique=True, index=True)
    title = Column(String)
    tag = Column(String)
    link = Column(String,index=True)


Base.metadata.create_all(bind=engine)


def add_feed_to_db(url: str, title: str, tag: str | None):
    feed = Feed(url=url)
    with SessionLocal() as session:
        session.add(Subscription(url=url, title=feed.title, tag=tag,link=feed.link))
        session.commit()
        session.close()


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
