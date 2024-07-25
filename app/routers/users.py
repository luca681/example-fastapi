from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from app import oath2 
from ..import schema, models, utils
from ..database import engine, get_db
from sqlalchemy.orm import session

router= APIRouter(tags=['users'])


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)

def create_user(User: schema.UserCreate, db: session= Depends(get_db)):

    #hash the password which is stored in User.password
    hashed_password= utils.hash(User.password)
    

    #replace the User's password with the hashed password
    User.password= hashed_password

    new_user=models.User(**User.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


# get a single user from the database using their assigned id
@router.get('/users/{id}', response_model=schema.UserOut)
def get_user(id: int, db: session= Depends(get_db), get_current_user: int=Depends(oath2.get_current_user)):
    user= db.query(models.User).filter(models.User.id== id).first()
    #if a user was not found
    if not user:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} does not exist')
    
    #if the user is found
    return user
