from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str | None
    published_at: datetime | None


# get all blogs
@app.get('/blogs')
async def index():
    return {
        'blogs': [
            {
                'title': 'Hello World of Programming!',
                'username': 'ravikumar2000'
            },
            {
                'title': 'Nice to CODE!!',
                'username': 'ravikumar2000'
            }
        ]
    }


# get a blog by id
@app.get('/blogs/{id}')
async def blog(id: int):
    return {
        'blog': {
            'id': id,
            'title': 'Nice to CODE!!',
            'username': 'ravikumar2000'
        }
    }

# store a blog
@app.post('/blogs')
async def storeBlog(blog: Blog):
    return blog
    return {'message': 'blog created successfully!'}