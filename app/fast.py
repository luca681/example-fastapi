from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from app import models 
from .database import engine, get_db
from .routers import posts, users, auth
from app.config import settings


models.Base.metadata.create_all(bind=engine)


app= FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)






