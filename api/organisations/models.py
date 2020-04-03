import uuid
from api.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from slugify import slugify

class Organisation(Base):

    __tablename__ = "organisations"
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True)
    slug = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.public_id = str(uuid.uuid4())
        self.name = name
        self.slug = slugify(name)

