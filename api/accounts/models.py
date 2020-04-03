import uuid
from api.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    disabled = Column(Boolean)

    def __init__(self, email, password):
        self.email = email
        self.password = password
