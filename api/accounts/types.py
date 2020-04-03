from pydantic import BaseModel


class Credentials(BaseModel):
    access_token: str
    refresh_token: str


class User(BaseModel):
    username: str
    email: str = None
    disabled: bool = None
