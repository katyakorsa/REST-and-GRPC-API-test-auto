from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
    status: StrictStr = Field(None)
    rating: Rating
    online: datetime = Field(None)
    name: StrictStr = Field(None)
    location: StrictStr = Field(None)
    registration: datetime = Field(None)


class UserEnvelopeModel(BaseModel):
    resource: Optional[User] = None
    metadata: str = Field(None)
