import uuid
from api.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON


class ContentType(Base):

    __tablename__ = "content_types"
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    fields = Column(JSON, nullable=False)

    def __init__(self, name, description, fields):
        self.public_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.fields = fields


class Entity(Base):

    __tablename__ = "entities"
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True)
    content_type_id = Column(Integer, ForeignKey("content_types.id"), nullable=False)
    value = Column(JSON, nullable=False)

    def __init__(self, content_type_id, value):
        self.public_id = str(uuid.uuid4())
        self.content_type_id = content_type_id
        self.value = value
