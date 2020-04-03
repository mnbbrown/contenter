from typing import List
from pydantic import BaseModel, Field


class ContentTypeField(BaseModel):
    name: str
    type: str


class ContentTypeRequest(BaseModel):
    name: str
    description: str = None
    content_fields: List[ContentTypeField] = Field([], alias="fields")


class ContentTypeResponse(ContentTypeRequest):
    id: str = Field("", alias="public_id")

    class Config:
        orm_mode = True
