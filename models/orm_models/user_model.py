from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from models.orm_models.base import Base


class User(Base):
    __tablename__ = 'Users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    RegistrationDate = Column(DateTime(True), nullable=False)
    LastVisitDate = Column(DateTime(True))
    TimezoneId = Column(Text)
    Role = Column(Integer, nullable=False)
    AccessPolicy = Column(Integer, nullable=False)
    Salt = Column(String(120))
    PasswordHash = Column(String(300))
    RatingDisabled = Column(Boolean, nullable=False)
    QualityRating = Column(Integer, nullable=False)
    QuantityRating = Column(Integer, nullable=False)
    Activated = Column(Boolean, nullable=False)
    CanMerge = Column(Boolean, nullable=False)
    MergeRequested = Column(UUID)
    IsRemoved = Column(Boolean, nullable=False)
    Status = Column(String(200))
    Name = Column(String(100))
    Location = Column(String(100))
    Icq = Column(String(20))
    Skype = Column(String(50))
    Info = Column(Text)
    ProfilePictureUrl = Column(String(200))
    MediumProfilePictureUrl = Column(String(200))
    SmallProfilePictureUrl = Column(String(200))
