from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from ..database import engine, SessionLocal, getDB
from ..schemas import Blog, ShowBlog, User, ShowUser
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..dependencies import *


router = APIRouter(
    prefix='/users',
    tags=['users'],
    dependencies=[]
)
hash_instance = Hash()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[ShowUser])
async def getUsers(db: Session = Depends(getDB)):
    return db.query(models.User).all()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
async def getUser(id: int, db: Session = Depends(getDB)):
    user = getUserByID(id, db).first()
    checkInstance(user)
    return user


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def storeUser(user: User, db: Session = Depends(getDB)):
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


@router.put('/', status_code=status.HTTP_202_ACCEPTED)
async def updateUser(id: int, user: User, db: Session = Depends(getDB)):
    old_user = getUserByID(id, db)
    checkInstance(old_user.first())
    hashed_password = hash_instance.encryptPassword(user.password)
    user.password = hashed_password
    old_user.update(user.dict(), synchronize_session=False)
    db.commit()
    return {'message': 'user updated successfully!'}
