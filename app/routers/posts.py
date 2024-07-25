from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import schema, models
from ..database import engine, get_db
from sqlalchemy.orm import session


router= APIRouter(tags=['posts'])


@router.get("/")
def read_root():
    return {"Hello": "Welcome to my first api, which i dedeicate to my mum. Amen"}


@router.get('/sqlalchemy')
def test_post(db: session =Depends(get_db)):
    return {'session status': 'succesful'}
    



