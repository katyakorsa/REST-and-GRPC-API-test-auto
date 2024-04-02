from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Comment(Base):
    __tablename__ = 'Comments'

    CommentId = Column(UUID, primary_key=True)
    EntityId = Column(UUID, nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateDate = Column(DateTime(True))
    Text = Column(String)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User')
