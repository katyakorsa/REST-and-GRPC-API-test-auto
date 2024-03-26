from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import UUID

from models.orm_models.base import Base


class Fora(Base):
    __tablename__ = 'Fora'

    ForumId = Column(UUID, primary_key=True)
    Title = Column(Text)
    Description = Column(Text)
    Order = Column(Integer, nullable=False)
    ViewPolicy = Column(Integer, nullable=False)
    CreateTopicPolicy = Column(Integer, nullable=False)
