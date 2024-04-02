from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class PendingPost(Base):
    __tablename__ = 'PendingPosts'

    PendingPostId = Column(UUID, primary_key=True)
    AwaitingUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    PendingUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)

    User = relationship('User', primaryjoin='PendingPost.AwaitingUserId == User.UserId')
    User1 = relationship('User', primaryjoin='PendingPost.PendingUserId == User.UserId')
    Room = relationship('Room')
