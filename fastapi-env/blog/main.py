from blog.routers import authentiction
from fastapi import FastAPI
from . import models
from .database import engine
from typing import List
from .routers import blog, users

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentiction.router)
app.include_router(blog.router)
app.include_router(users.router)