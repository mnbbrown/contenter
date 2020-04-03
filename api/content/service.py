from marshmallow import Schema, fields
from typing import List
from api.content.types import ContentTypeField
from api.content.models import ContentType


def create_field(field):
    return {
        "string": fields.String(),
        "int": fields.Integer(),
        "email": fields.Email(),
        "datetime": fields.DateTime(),
        "boolean": fields.Boolean(),
        "time": fields.Time(),
        "dict": fields.Dict(),
        "url": fields.Url(),
    }.get(field)


def generate_schema(fields: List[ContentTypeField]):
    fields = {field.get("name"): create_field(field.get("type")) for field in fields}
    return Schema.from_dict(fields)


def validate_entity(entity: dict, fields: List[ContentTypeField]) -> bool:
    Schema = generate_schema(fields)
    return Schema().validate(entity)
