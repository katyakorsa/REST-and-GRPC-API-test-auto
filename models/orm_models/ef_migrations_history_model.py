from sqlalchemy import Column, String

from models.orm_models.base import Base


class EFMigrationsHistory(Base):
    __tablename__ = '__EFMigrationsHistory'

    MigrationId = Column(String(150), primary_key=True)
    ProductVersion = Column(String(32), nullable=False)
