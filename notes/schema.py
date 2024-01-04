from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
    is_public: bool


class User(BaseModel):
    name : str
    email: str
    username: str
    password: str
    