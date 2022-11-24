from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from ..database import engine, SessionLocal, getDB
from ..schemas import Blog, ShowBlog, User, ShowUser
from .. import models
from sqlalchemy.orm import Session
from ..dependencies import *

router = APIRouter()


@router.get('/blogs', status_code=status.HTTP_200_OK, response_model=list[ShowBlog], tags=['blogs'])
async def getBlogs(db: Session = Depends(getDB)):
    return db.query(models.Blog).all()


@router.get('/blogs/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
async def getBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db).first()
    checkInstance(blog)
    return blog


@router.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
async def storeBlog(blog: Blog, db: Session = Depends(getDB)):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body,
        user_id=blog.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
async def updateBlog(id: int, blog: Blog, db: Session = Depends(getDB)):
    old_blog = getBlogByID(id, db)
    checkInstance(old_blog.first())
    old_blog.update(blog.dict(), synchronize_session=False)
    db.commit()
    return {'message': 'blog updated successfully!'}


@router.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
async def deleteBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db)
    checkInstance(blog.first())
    blog.delete(synchronize_session=False)
    db.commit()
