from typing import Union

from data.dataclass_factory import Book, Author
from data.pydantic import PydanticBook, PydanticAuthor


def get_book(default: bool) -> Union[Book, PydanticBook]:
    if default:
        return PydanticBook(
            title="A Book",
            author=PydanticAuthor(
                name="Me",
                email="me@author.book"
            ),
            price=249
        )
    else:
        return Book(
            title="A Book",
            author=Author(
                name="Me",
                email="me@author.book"
            ),
            price=249
        )