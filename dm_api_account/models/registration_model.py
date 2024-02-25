from pydantic import BaseModel, StrictStr, Field
from typing import Optional


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr
