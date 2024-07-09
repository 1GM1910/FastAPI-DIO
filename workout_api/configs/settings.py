from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:crisegu190400@localhost/workout')
    

settings = Settings()