from fastapi import FastAPI, APIRouter, Depends
from pydantic import EmailStr
from ..schemas import Token, TokenData
from sqlalchemy.orm import Session
from ..database import getDB
from ..controllers import authentication_controller
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def loginUser(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getDB)):
    return authentication_controller.loginUser(db, request)