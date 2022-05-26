from typing import Text

from dataclass_factory import Factory

import data
from measurer import Measurer

measurer = Measurer("Serialize to JSON")


def pydantic() -> Text:
    book = data.get_book(default=True)

    result = measurer.time_it("Serialize with Pydantic", book.json)

    return result


def dataclass_factory() -> Text:
    factory = Factory()

    book = data.get_book(default=False)

    result = measurer.time_it("Serialize with dataclass_factory", factory.dump, book, data.Book)

    return result


def test() -> None:
    pydantic()

    dataclass_factory()

    measurer.visualize()
