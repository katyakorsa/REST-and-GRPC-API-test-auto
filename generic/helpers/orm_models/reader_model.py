from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Reader(Base):
    __tablename__ = 'Readers'

    ReaderId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    Game = relationship('Game')
    User = relationship('User')
