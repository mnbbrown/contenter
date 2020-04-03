from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from api.database import get_db
from api.content import service
from api.content import repository
from api.content.types import ContentTypeRequest, ContentTypeResponse

router = APIRouter()


@router.get("/", response_model=List[ContentTypeResponse], response_model_by_alias=False)
def list_content_types(db: Session = Depends(get_db)):
    return repository.list_content_types(db)


@router.post("/", response_model=ContentTypeResponse, response_model_by_alias=False)
def create_content_type(content_type: ContentTypeRequest, db: Session = Depends(get_db)):
    return repository.save_content_type(db, content_type)


@router.get("/{content_type_id}")
def get_content_type(content_type_id: str, db: Session = Depends(get_db)):
    return repository.get_content_type(db, content_type_id)


@router.post("/{content_type_id}/entities")
def create_entity(content_type_id: str, entity: dict, db: Session = Depends(get_db)):
    content_type = repository.get_content_type(db, content_type_id)
    entities = repository.list_entities(db, content_type.id)
    service.validate_entity(entity, content_type)
    return repository.save_entity(db, content_type_id, entity)


@router.get("/{content_type_id}/entities")
def list_entities(content_type_id: str, db: Session = Depends(get_db)):
    content_type = repository.get_content_type(db, content_type_id)
    entities = repository.list_entities(db, content_type.id)
    schema = service.generate_schema(content_type.fields)
    return schema(many=True).dump([entity.value for entity in entities])
