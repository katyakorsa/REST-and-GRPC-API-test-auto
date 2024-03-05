from __future__ import annotations

from pydantic import BaseModel, StrictStr, Field, Extra
from typing import Optional


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(
        None,
        description='Login'
    )
    email: Optional[StrictStr] = Field(
        None,
        description='Email'
    )
    password: Optional[StrictStr] = Field(
        None,
        description='Password'
    )
