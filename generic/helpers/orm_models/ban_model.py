from sqlalchemy import Column, Boolean, Integer, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Ban(Base):
    __tablename__ = 'Bans'

    BanId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ModeratorId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    StartDate = Column(DateTime(True), nullable=False)
    EndDate = Column(DateTime(True), nullable=False)
    Comment = Column(Text)
    AccessRestrictionPolicy = Column(Integer, nullable=False)
    IsVoluntary = Column(Boolean, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Ban.ModeratorId == User.UserId')
    User1 = relationship('User', primaryjoin='Ban.UserId == User.UserId')
