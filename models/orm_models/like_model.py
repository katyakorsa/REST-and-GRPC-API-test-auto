from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Like(Base):
    __tablename__ = 'Likes'

    LikeId = Column(UUID, primary_key=True)
    EntityId = Column(UUID, nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    User = relationship('User')
