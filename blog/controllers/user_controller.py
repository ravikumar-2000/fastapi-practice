from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import models, dependencies, schemas


hash_instance = Hash()


def getUsers(db: Session):
    return db.query(models.User).all()


def getUser(db: Session, id: int):
    user = dependencies.getUserByID(id, db).first()
    dependencies.checkInstance(user)
    return user


def storeUser(db: Session, user: schemas.User):
    hashed_password = hash_instance.encryptPassword(user.password)
    new_user = models.User(
        username=user.username, email=user.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def updateUser(db: Session, id: int, user: schemas.User):
    old_user = dependencies.getUserByID(id, db)
    dependencies.checkInstance(old_user.first())
    hashed_password = hash_instance.encryptPassword(user.password)
    user.password = hashed_password
    old_user.update(user.dict(), synchronize_session=False)
    db.commit()
    return {"message": "user updated successfully!"}
