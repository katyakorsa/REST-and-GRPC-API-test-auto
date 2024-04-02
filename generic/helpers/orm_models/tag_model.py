from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Tag(Base):
    __tablename__ = 'Tags'

    TagId = Column(UUID, primary_key=True)
    TagGroupId = Column(ForeignKey('TagGroups.TagGroupId', ondelete='CASCADE'), nullable=False, index=True)
    Title = Column(Text)

    TagGroup = relationship('TagGroup')
