from __future__ import annotations

from pydantic import BaseModel, StrictStr, Field, Extra
from typing import Optional


class LoginCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    remember_me: Optional[bool] = Field(
        None,
        alias='rememberMe'
    )
