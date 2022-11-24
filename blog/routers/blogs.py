from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from ..database import engine, SessionLocal, getDB
from ..schemas import Blog, ShowBlog, User, ShowUser
from sqlalchemy.orm import Session
from ..controllers import blog_controller
from .. import oauth2

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShowBlog])
async def getBlogs(db: Session = Depends(getDB), current_user: User = Depends(oauth2.get_current_user)):
    return blog_controller.getBlogs(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlog)
async def getBlog(id: int, db: Session = Depends(getDB), current_user: User = Depends(oauth2.get_current_user)):
    return blog_controller.getBlog(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def storeBlog(blog: Blog, db: Session = Depends(getDB), current_user: User = Depends(oauth2.get_current_user)):
    return blog_controller.storeBlog(db, blog)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def updateBlog(id: int, blog: Blog, db: Session = Depends(getDB), current_user: User = Depends(oauth2.get_current_user)):
    return blog_controller.updateBlog(db, id, blog)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteBlog(id: int, db: Session = Depends(getDB), current_user: User = Depends(oauth2.get_current_user)):
    blog_controller.deleteBlog(db, id)
