import pytest
import unittest
from starlette.testclient import TestClient
from api import app
from api.database import Base, engine, context_session

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)
