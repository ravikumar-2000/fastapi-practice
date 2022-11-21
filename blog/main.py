from fastapi import FastAPI, Depends, status, HTTPException
from .database import engine, SessionLocal, getDB
from .schemas import Blog, ShowBlog, User, ShowUser
from . import models
from .hashing import Hash
from sqlalchemy.orm import Session

app = FastAPI()

# this is to create all the tables defined as classes in models.py file
models.Base.metadata.create_all(bind=engine)


def getBlogByID(id, db):
    return db.query(models.Blog).filter(models.Blog.id == id)


def getUserByID(id, db):
    return db.query(models.User).filter(models.User.id == id)


def checkInstance(instance):
    if not instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='instance not found')


@app.get('/blogs', status_code=status.HTTP_200_OK, response_model=list[ShowBlog], tags=['blogs'])
async def getBlogs(db: Session = Depends(getDB)):
    return db.query(models.Blog).all()


@app.get('/blogs/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
async def getBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db).first()
    checkInstance(blog)
    return blog


@app.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
async def storeBlog(blog: Blog, db: Session = Depends(getDB)):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
async def updateBlog(id: int, blog: Blog, db: Session = Depends(getDB)):
    old_blog = getBlogByID(id, db)
    checkInstance(old_blog.first())
    old_blog.update(blog.dict(), synchronize_session=False)
    db.commit()
    return {'message': 'blog updated successfully!'}


@app.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
async def deleteBlog(id: int, db: Session = Depends(getDB)):
    blog = getBlogByID(id, db)
    checkInstance(blog.first())
    blog.delete(synchronize_session=False)
    db.commit()


@app.get('/users', status_code=status.HTTP_200_OK, response_model=list[ShowUser], tags=['users'])
async def getUsers(db: Session = Depends(getDB)):
    return db.query(models.User).all()


@app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser, tags=['users'])
async def getUser(id: int, db: Session = Depends(getDB)):
    user = getUserByID(id, db).first()
    checkInstance(user)
    return user


@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=ShowUser, tags=['users'])
async def storeUser(user: User, db: Session = Depends(getDB)):
    hash_instance = Hash()
    hashed_password = hash_instance.encryptPassword(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


