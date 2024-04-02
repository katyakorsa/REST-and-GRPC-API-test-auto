from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class RoomClaim(Base):
    __tablename__ = 'RoomClaims'

    RoomClaimId = Column(UUID, primary_key=True)
    ParticipantId = Column(ForeignKey('Characters.CharacterId', ondelete='CASCADE'),
                           ForeignKey('Readers.ReaderId', ondelete='CASCADE'), nullable=False, index=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    Policy = Column(Integer, nullable=False)

    Reader = relationship('Reader')
    Character = relationship('Character')
    Room = relationship('Room')
