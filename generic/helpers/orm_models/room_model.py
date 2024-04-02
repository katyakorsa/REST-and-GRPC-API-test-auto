from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Room(Base):
    __tablename__ = 'Rooms'

    RoomId = Column(UUID, primary_key=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    Title = Column(Text)
    AccessType = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    OrderNumber = Column(Float(53), nullable=False)
    PreviousRoomId = Column(ForeignKey('Rooms.RoomId', ondelete='RESTRICT'), index=True)
    NextRoomId = Column(ForeignKey('Rooms.RoomId', ondelete='RESTRICT'), unique=True)
    IsRemoved = Column(Boolean, nullable=False)

    Game = relationship('Game')
    parent = relationship('Room', remote_side=[RoomId], primaryjoin='Room.NextRoomId == Room.RoomId')
    parent1 = relationship('Room', remote_side=[RoomId], primaryjoin='Room.PreviousRoomId == Room.RoomId')
