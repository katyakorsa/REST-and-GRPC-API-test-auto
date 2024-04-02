from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class GameTag(Base):
    __tablename__ = 'GameTags'

    GameTagId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    TagId = Column(ForeignKey('Tags.TagId', ondelete='CASCADE'), nullable=False, index=True)

    Game = relationship('Game')
    Tag = relationship('Tag')
