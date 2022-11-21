from pydantic import BaseModel
from datetime import datetime


class Blog(BaseModel):
    title: str
    body: str | None = None


class ShowBlog(Blog):
    published_at: datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
