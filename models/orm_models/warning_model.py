from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Warning(Base):
    __tablename__ = 'Warnings'

    WarningId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ModeratorId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    EntityId = Column(UUID, nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(String)
    Points = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Warning.ModeratorId == User.UserId')
    User1 = relationship('User', primaryjoin='Warning.UserId == User.UserId')
