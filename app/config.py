from pydantic_settings import BaseSettings

#sets up environment variable as a security measure

class Settings(BaseSettings):
    database_hostname: str
    database_port:str
    database_password: str 
    database_name: str 
    database_username: str
    SECRET_KEY: str 
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file= ".env"

settings= Settings()
