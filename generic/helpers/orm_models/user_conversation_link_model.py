from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class UserConversationLink(Base):
    __tablename__ = 'UserConversationLinks'

    UserConversationLinkId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    ConversationId = Column(ForeignKey('Conversations.ConversationId', ondelete='CASCADE'), nullable=False, index=True)
    IsRemoved = Column(Boolean, nullable=False)

    Conversation = relationship('Conversation')
    User = relationship('User')
