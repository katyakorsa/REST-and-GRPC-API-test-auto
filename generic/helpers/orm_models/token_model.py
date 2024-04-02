from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Token(Base):
    __tablename__ = 'Tokens'

    TokenId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    EntityId = Column(UUID, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User')
