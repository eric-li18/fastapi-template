from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Creates database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base will be inherited to create DB models
Base = declarative_base()