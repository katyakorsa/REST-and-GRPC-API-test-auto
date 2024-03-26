from sqlalchemy import Column, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.orm_models.base import Base


class Report(Base):
    __tablename__ = 'Reports'

    ReportId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    TargetId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    ReportText = Column(Text)
    Comment = Column(Text)
    AnswerAuthorId = Column(ForeignKey('Users.UserId', ondelete='RESTRICT'), index=True)
    Answer = Column(Text)

    User = relationship('User', primaryjoin='Report.AnswerAuthorId == User.UserId')
    User1 = relationship('User', primaryjoin='Report.TargetId == User.UserId')
    User2 = relationship('User', primaryjoin='Report.UserId == User.UserId')
