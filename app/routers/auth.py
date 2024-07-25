from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import models

from .. import database, schema, utils, oath2, models



router=APIRouter(tags=['Authentication'])

@router.post('/login')
#note that OAuth2PasswordRequestForm replaces schema.UserLogin, which stores login details like email and password. email is now username,where it is stored by OAuth2PasswordRequestForm
def login(User_credentials: OAuth2PasswordRequestForm=Depends(), db: session= Depends(database.get_db)):
    usser= db.query(models.User).filter(models.User.email==User_credentials.username).first()
    if not usser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    if not utils.verify(User_credentials.password, usser.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create token
    #return token

    access_token= oath2.create_access_token(data={"user_id": usser.id})
    return {"access_token": access_token, "token_type": "bearer"}
