from . import models
from fastapi import status, HTTPException


def getBlogByID(id, db):
    return db.query(models.Blog).filter(models.Blog.id == id)


def getUserByID(id, db):
    return db.query(models.User).filter(models.User.id == id)


def checkInstance(instance):
    if not instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='instance not found')
