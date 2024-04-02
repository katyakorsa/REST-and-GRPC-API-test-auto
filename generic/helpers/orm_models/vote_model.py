from sqlalchemy import Column, Integer, DateTime, ForeignKey, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Vote(Base):
    __tablename__ = 'Votes'

    VoteId = Column(UUID, primary_key=True)
    PostId = Column(ForeignKey('Posts.PostId', ondelete='CASCADE'), nullable=False, index=True)
    GameId = Column(ForeignKey('Games.GameId', ondelete='CASCADE'), nullable=False, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    TargetUserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Type = Column(Integer, nullable=False)
    SignValue = Column(SmallInteger, nullable=False)

    Game = relationship('Game')
    Post = relationship('Post')
    User = relationship('User', primaryjoin='Vote.TargetUserId == User.UserId')
    User1 = relationship('User', primaryjoin='Vote.UserId == User.UserId')
