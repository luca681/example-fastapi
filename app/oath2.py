from jose import JWTError, jwt
from datetime import timedelta, datetime
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from app import schema
from fastapi.security import OAuth2PasswordBearer

oath2_scheme= OAuth2PasswordBearer(tokenUrl='login')

#SECRET_KEY
#ALGORITHM
#EXPIRATION TIME

SECRET_KEY= "jbjkbfdiofhjhdhslhddfdfhwuheuluehuihfuhfuufhfhfehol"
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 30

def create_access_token(data: dict):
    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")
    #make a copy of the data to avoid changing it accidentaly
    to_encode= data.copy()

    expire=datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

#verifies the validity of the access token, user_id" is defined in access_token, auth.py
def verify_access_token(token: str, credentials_exception):
    
    try:

        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str =payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data= schema.TokenData(id=id)
    
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token: str=Depends(oath2_scheme)):
    credentials_exception=HTTPException(status.HTTP_401_UNAUTHORIZED_, detail=f"could not validate credentials", headers={"www-Authenticate": "Bearer"}) 
    return verify_access_token(token, credentials_exception)