import pytest
from starlette.config import environ

environ["TESTING"] = "TRUE"

from api.database import Base, engine, context_session
from starlette.testclient import TestClient
from api import app

@pytest.fixture(scope="function")
def db(request):
    with context_session() as session:
        yield session

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(engine)
    client = TestClient(app)
    yield client
    Base.metadata.drop_all(engine)
