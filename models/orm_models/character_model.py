from sqlalchemy import Column, Boolean, Integer, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Character(Base):
    __tablename__ = 'Characters'

    CharacterId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    Status = Column(Integer, nullable=False)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Name = Column(Text)
    Race = Column(Text)
    Class = Column(Text)
    Alignment = Column(Integer)
    Appearance = Column(Text)
    Temper = Column(Text)
    Story = Column(Text)
    Skills = Column(Text)
    Inventory = Column(Text)
    IsNpc = Column(Boolean, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    Game = relationship('Game')
    User = relationship('User')
