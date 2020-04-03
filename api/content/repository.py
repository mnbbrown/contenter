from typing import List
from api.content.types import ContentTypeRequest, ContentTypeResponse
from api.content.models import ContentType, Entity
from sqlalchemy.orm import Session


def save_content_type(db: Session, value: ContentTypeRequest) -> ContentType:
    content_type = ContentType(value.name, value.description, [field.dict() for field in value.content_fields])
    db.add(content_type)
    db.flush()
    return content_type


def list_content_types(db: Session) -> List[ContentType]:
    return db.query(ContentType).all()

def get_content_type(db: Session, content_type_id: str) -> ContentType:
    return db.query(ContentType).filter(ContentType.public_id == content_type_id).first()


def save_entity(db: Session, content_type_id: int, value: dict) -> Entity:
    entity = Entity(content_type_id, entity)
    db.add(entity)
    db.flush()
    return entity


def list_entities(db: Session, content_type_id: int) -> List[Entity]:
    return db.query(Entity).filter(Entity.content_type_id == content_type_id).all()
