from fastapi import FastAPI, Depends, status, HTTPException
from .database import engine, SessionLocal, getDB
from .schemas import Blog
from . import models
from sqlalchemy.orm import Session

app = FastAPI()

# this is to create all the tables defined as classes in models.py file
models.Base.metadata.create_all(bind=engine)


def getBlogByID(id, db):
    return db.query(models.Blog).filter(models.Blog.id == id)


def checkBlog(blog):
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='blog not found')


@app.get('/blogs', status_code=status.HTTP_200_OK)
async def getBlogs(db: Session = Depends(getDB)):
    return db.query(models.Blog).all()


@app.get('/blogs/{id}', status_code=status.HTTP_200_OK)
async def getBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db).first()
    checkBlog(blog)
    return blog


@app.post('/blogs', status_code=status.HTTP_201_CREATED)
async def storeBlog(blog: Blog, db: Session = Depends(getDB)):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED)
async def updateBlog(id: int, blog: Blog, db: Session = Depends(getDB)):
    old_blog = getBlogByID(id, db)
    checkBlog(old_blog.first())
    old_blog.update(dict(blog), synchronize_session=False)
    db.commit()


@app.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db)
    checkBlog(blog.first())
    blog.delete(synchronize_session=False)
    db.commit()
