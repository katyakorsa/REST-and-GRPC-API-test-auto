from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Post(Base):
    __tablename__ = 'Posts'

    PostId = Column(UUID, primary_key=True)
    RoomId = Column(ForeignKey('Rooms.RoomId', ondelete='CASCADE'), nullable=False, index=True)
    CharacterId = Column(ForeignKey('Characters.CharacterId', ondelete='RESTRICT'), index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    LastUpdateUserId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    LastUpdateDate = Column(DateTime(True))
    Text = Column(String)
    Commentary = Column(Text)
    MasterMessage = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)

    Character = relationship('Character')
    User = relationship('User', primaryjoin='Post.LastUpdateUserId == User.UserId')
    Room = relationship('Room')
    User1 = relationship('User', primaryjoin='Post.UserId == User.UserId')
