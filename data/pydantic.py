from pydantic import BaseModel


class PydanticAuthor(BaseModel):
    name: str
    email: str


class PydanticBook(BaseModel):
    title: str
    author: PydanticAuthor
    price: int
