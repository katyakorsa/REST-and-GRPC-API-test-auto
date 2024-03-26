from sqlalchemy import Column, Boolean, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Conversation(Base):
    __tablename__ = 'Conversations'

    ConversationId = Column(UUID, primary_key=True)
    LastMessageId = Column(ForeignKey('Messages.MessageId', ondelete='RESTRICT'), index=True)
    Visavi = Column(Boolean, nullable=False, server_default=Text("false"))

    Message = relationship('Message', primaryjoin='Conversation.LastMessageId == Message.MessageId')
