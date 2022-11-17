import datetime
from .database import Base
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import relationship


class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(500))
    published_at = Column(DateTime, default=datetime.datetime.utcnow)