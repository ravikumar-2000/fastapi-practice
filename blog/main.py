from fastapi import FastAPI
from .database import engine
from . import models
from .routers import users, blogs, authentication

app = FastAPI()
app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(authentication.router)

# this is to create all the tables defined as classes in models.py file
models.Base.metadata.create_all(bind=engine)
