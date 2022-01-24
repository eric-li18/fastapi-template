import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..db.session import SessionLocal


@pytest.fixture(scope="session")
def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client():
    testclient = TestClient(app)
    yield testclient
