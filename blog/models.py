import datetime
from .database import Base
from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(50))
    body = Column(String(500), nullable=True)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)

    creator = relationship('User', back_populates='blogs')

    def __str__(self):
        return f'{title} {str(published_at)}'


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    blogs = relationship('Blog', back_populates='creator')


