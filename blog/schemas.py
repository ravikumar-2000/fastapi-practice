from pydantic import BaseModel
from datetime import datetime


class Blog(BaseModel):
    title: str
    body: str | None
    published_at: datetime | None
