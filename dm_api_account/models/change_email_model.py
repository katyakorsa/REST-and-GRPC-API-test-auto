from pydantic import BaseModel, StrictStr, Field


class ChangeEmailModel(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr
