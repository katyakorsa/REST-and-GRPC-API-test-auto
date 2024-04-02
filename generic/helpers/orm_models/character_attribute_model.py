from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class CharacterAttribute(Base):
    __tablename__ = 'CharacterAttributes'

    CharacterAttributeId = Column(UUID, primary_key=True)
    AttributeId = Column(UUID, nullable=False)
    CharacterId = Column(ForeignKey('Characters.CharacterId', ondelete='CASCADE'), nullable=False, index=True)
    Value = Column(Text)

    Character = relationship('Character')
