from fastapi import FastAPI
from .database import engine
from .schemas import Blog
from . import models

app = FastAPI()

# this is to create all the tables defined as classes in models.py file
models.Base.metadata.create_all(bind=engine)

@app.post('/blogs')
async def storeBlog(blog: Blog):
    return blog
    return {'message': 'blog saved successfully!'}