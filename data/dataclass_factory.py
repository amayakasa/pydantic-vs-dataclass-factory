from dataclasses import dataclass


@dataclass
class Author:
    name: str
    email: str


@dataclass
class Book:
    title: str
    author: Author
    price: int
