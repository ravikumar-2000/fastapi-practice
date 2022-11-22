from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class Blog(BaseModel):
    title: str
    body: str | None = None
    user_id: int

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    blogs: list[Blog]

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str | None = None
    published_at: datetime
    creator: ShowUser

    class Config:
        orm_mode = True
