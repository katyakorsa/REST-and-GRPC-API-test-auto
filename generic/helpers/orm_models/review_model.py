from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from generic.helpers.orm_models.base import Base


class Review(Base):
    __tablename__ = 'Reviews'

    ReviewId = Column(UUID, primary_key=True)
    UserId = Column(ForeignKey('Users.UserId', ondelete='CASCADE'), nullable=False, index=True)
    CreateDate = Column(DateTime(True), nullable=False)
    Text = Column(String)
    IsApproved = Column(Boolean, nullable=False)
    # IsRemoved = Column(Boolean, nullable=False, server_default=Text("false"))

    User = relationship('User')
