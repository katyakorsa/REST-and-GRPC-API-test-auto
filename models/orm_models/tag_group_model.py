from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from models.orm_models.base import Base


class TagGroup(Base):
    __tablename__ = 'TagGroups'

    TagGroupId = Column(UUID, primary_key=True)
    Title = Column(Text)
