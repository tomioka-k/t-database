from ninja import Schema, Field
from typing import List


class SourceSchema(Schema):
    id: int
    name: str


class CategorySchema(Schema):
    id: int
    name: str


class TagSchema(Schema):
    id: int
    name: str


class VideoSchema(Schema):
    id: int
    category: str = Field(None, alias="category.name")
    name: str
    tag: List[TagSchema]
    source: str = Field(None, alias="source.name")


class VideoFilters(Schema):
    limit: int = 100
    offset: int = 0
    category_id: int = None
    source_id: int = None
    tag__in: List[int] = None

