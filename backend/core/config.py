from typing import Optional
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_USER: str


settings = Settings()