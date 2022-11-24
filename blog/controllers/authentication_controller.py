from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, dependencies, hashing, jwt_token


hash_instance = hashing.Hash()


def loginUser(db: Session, request: OAuth2PasswordRequestForm = Depends()):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    dependencies.checkInstance(user)
    if not hash_instance.verifyPassword(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    access_token = jwt_token.create_access_token(data={'email': request.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
