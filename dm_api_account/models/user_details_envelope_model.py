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


class Paging(BaseModel):
    posts_per_page: int = Field(alias="postsPerPage")
    comments_per_page: int = Field(alias="commentsPerPage")
    topics_per_page: int = Field(alias="topicsPerPage")
    messages_per_page: int = Field(alias="messagesPerPage")
    entities_per_page: int = Field(alias="entitiesPerPage")


class Settings(BaseModel):
    color_schema: str = Field(alias="")
    nanny_greetings_message: str = Field(alias="nannyGreetingsMessage")
    paging: Paging


class Info(BaseModel):
    value: str
    parse_mode: str = Field(alias="parseMode")


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class UserDetails(BaseModel):
    login: str
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: str
    rating: Rating
    online: datetime
    name: str
    location: str
    registration: datetime
    icq: str
    skype: str
    original_picture_url: str = Field(alias="originalPictureUrl")
    info: Info
    settings: Settings


class UserDetailsEnvelopeModel(BaseModel):
    resource: UserDetails
    metadata: str = Field(None)
