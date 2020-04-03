import pytest
import unittest
from api.content import service
from marshmallow.exceptions import ValidationError


def test_generate_schema():
    schema_json = [{"name": "name", "type": "string"}]
    GeneratedSchema = service.generate_schema(schema_json)
    schema = GeneratedSchema()
    schema.load({"name": "test"})
    with pytest.raises(ValidationError):
        schema.load({"name": 1})

def test_validate_entity():
    fields = [{"name": "name", "type": "string"}]
    assert len(service.validate_entity({"name": "test"}, fields).keys()) == 0
    assert len(service.validate_entity({"name": 1}, fields).keys()) == 1

def test_field_types():
    examples = {"string": "string", "int": 1, "email": "test@test.com"}
    content_type = [{"type": v, "name": v} for v in examples.keys()]
    schema = service.generate_schema(content_type)
    result = schema().load(examples)
    with pytest.raises(ValidationError):
        bad_examples = {"string": 0.2, "int": "1", "email": "test123"}
        schema().load(bad_examples)
