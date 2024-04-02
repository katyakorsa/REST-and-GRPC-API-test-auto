from sqlalchemy import Column, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Upload(Base):
    __tablename__ = 'Uploads'

    UploadId = Column(UUID, primary_key=True)
    CreateDate = Column(DateTime(True), nullable=False)
    EntityId = Column(UUID, index=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    FilePath = Column(Text)
    FileName = Column(Text)
    IsRemoved = Column(Boolean, nullable=False)
    Original = Column(Boolean, nullable=False, server_default=text("false"))

    User = relationship('User')
