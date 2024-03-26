from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Message(Base):
    __tablename__ = 'Messages'

    MessageId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ConversationId = Column(ForeignKey('Conversations.ConversationId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(String)
    IsRemoved = Column(Boolean, nullable=False)

    Conversation = relationship('Conversation', primaryjoin='Message.ConversationId == Conversation.ConversationId')
    User = relationship('User')
