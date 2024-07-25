from passlib.context import CryptContext

#this code hashes the password and works from importing CryptoContext from passlib.context
pwd_context=CryptContext(schemes=["bcrypt"], deprecated='auto')

#the function below hashes the password before being stored in the database
def hash(password: str):
    return pwd_context.hash(password)

#the function below hashes the password from the user from a login attempt, which is then compared to the hashed password in the database for authentication

def verify (plain_password , hashed_password):
    return pwd_context.verify(plain_password, hashed_password)