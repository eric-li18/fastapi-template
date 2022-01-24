from fastapi import FastAPI
from .routers import *
from .db.init_db import init_db

init_db()

app = FastAPI()

app.include_router(item.router, prefix="/items", tags=["Items"])