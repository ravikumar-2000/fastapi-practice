from sqlalchemy.orm import Session
from .. import models, dependencies, schemas


def getBlogs(db: Session):
    return db.query(models.Blog).all()


def getBlog(db: Session, id: int):
    blog = dependencies.getBlogByID(id, db).first()
    dependencies.checkInstance(blog)
    return blog


def storeBlog(db: Session, blog: schemas.Blog):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def updateBlog(db: Session, id: int, blog: schemas.Blog):
    old_blog = dependencies.getBlogByID(id, db)
    dependencies.checkInstance(old_blog.first())
    old_blog.update(blog.dict(), synchronize_session=False)
    db.commit()
    return {"message": "blog updated successfully!"}


def deleteBlog(db: Session, id: int):
    blog = dependencies.getBlogByID(id, db)
    dependencies.checkInstance(blog.first())
    blog.delete(synchronize_session=False)
    db.commit()
