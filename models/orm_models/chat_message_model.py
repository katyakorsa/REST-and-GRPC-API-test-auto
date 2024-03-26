from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class ChatMessage(Base):
    __tablename__ = 'ChatMessages'

    ChatMessageId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(String)

    User = relationship('User')
