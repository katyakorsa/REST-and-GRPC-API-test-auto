from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class ForumModerator(Base):
    __tablename__ = 'ForumModerators'

    ForumModeratorId = Column(UUID, primary_key=True)
    ForumId = Column(ForeignKey('Fora.ForumId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)

    Fora = relationship('Fora')
    User = relationship('User')
