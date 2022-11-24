from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from ..database import engine, SessionLocal, getDB
from ..schemas import Blog, ShowBlog, User, ShowUser
from sqlalchemy.orm import Session
from ..controllers import user_controller


router = APIRouter(prefix="/users", tags=["users"], dependencies=[])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShowUser])
async def getUsers(db: Session = Depends(getDB)):
    return user_controller.getUsers(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUser)
async def getUser(id: int, db: Session = Depends(getDB)):
    return user_controller.getUser(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def storeUser(user: User, db: Session = Depends(getDB)):
    return user_controller.storeUser(db, user)


@router.put("/", status_code=status.HTTP_202_ACCEPTED)
async def updateUser(id: int, user: User, db: Session = Depends(getDB)):
    return user_controller.updateUser(db, id, user)
