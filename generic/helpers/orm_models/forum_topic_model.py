from sqlalchemy import Column, Boolean, DateTime, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class ForumTopic(Base):
    __tablename__ = 'ForumTopics'

    ForumTopicId = Column(UUID, primary_key=True)
    ForumId = Column(ForeignKey('Fora.ForumId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Title = Column(Text)
    Text = Column(String)
    Attached = Column(Boolean, nullable=False)
    Closed = Column(Boolean, nullable=False)
    LastCommentId = Column(ForeignKey('Comments.CommentId', ondelete='RESTRICT'), index=True)
    IsRemoved = Column(Boolean, nullable=False)

    Fora = relationship('Fora')
    Comment = relationship('Comment')
    User = relationship('User')
