from enum import unique
from sqlalchemy import Column, String, Integer, column, true

from base import Base

class Article(Base):
    __tablename__='articles'
    #estructurar nuestros datos -> labor principal de un ingeniero de datos
    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title =  Column(String)
    newspaper_uid =  Column(String)
    n_tokens_body = Column(Integer)
    n_tokens_title = Column(Integer)
    url =  Column(String, unique = True)

    def __init__(self, uid, body, host, newspaper_uid, n_tokens_body, n_tokens_title, title, url) -> None:
        self.id = uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.n_tokens_body = n_tokens_body
        self.n_tokens_title = n_tokens_title
        self.url = url
        