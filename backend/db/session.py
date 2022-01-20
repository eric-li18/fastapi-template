from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

if not database_exists(settings.SQLALCHEMY_DATABASE_URI):
    create_database(settings.SQLALCHEMY_DATABASE_URI)

# Creates database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)