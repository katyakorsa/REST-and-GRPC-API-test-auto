from pydantic import BaseModel, StrictStr, Field
from typing import Optional


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: bool
