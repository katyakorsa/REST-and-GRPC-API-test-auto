from sqlalchemy import Column, Boolean, Integer, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Game(Base):
    __tablename__ = 'Games'

    GameId = Column(UUID, primary_key=True)
    CreateDate = Column(DateTime(True), nullable=False)
    ReleaseDate = Column(DateTime(True))
    Status = Column(Integer, nullable=False)
    MasterId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    AssistantId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    NannyId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    AttributeSchemaId = Column(UUID)
    Title = Column(Text)
    SystemName = Column(Text)
    SettingName = Column(Text)
    Info = Column(Text)
    HideTemper = Column(Boolean, nullable=False)
    HideSkills = Column(Boolean, nullable=False)
    HideInventory = Column(Boolean, nullable=False)
    HideStory = Column(Boolean, nullable=False)
    DisableAlignment = Column(Boolean, nullable=False)
    HideDiceResult = Column(Boolean, nullable=False)
    ShowPrivateMessages = Column(Boolean, nullable=False)
    CommentariesAccessMode = Column(Integer, nullable=False)
    Notepad = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)

    User = relationship('User', primaryjoin='Game.AssistantId == User.UserId')
    User1 = relationship('User', primaryjoin='Game.MasterId == User.UserId')
    User2 = relationship('User', primaryjoin='Game.NannyId == User.UserId')
