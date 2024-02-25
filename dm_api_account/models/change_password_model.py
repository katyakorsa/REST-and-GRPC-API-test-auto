from pydantic import BaseModel, StrictStr


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    old_password: StrictStr
    new_password: StrictStr
