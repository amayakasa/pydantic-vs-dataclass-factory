from dataclass_factory import Factory

from data import PydanticBook, Book
from measurer import Measurer
from tests import serialize

measurer: Measurer = Measurer("Parsing from JSON")


def pydantic() -> PydanticBook:
    book = serialize.pydantic()

    result = measurer.time_it("Serialize with Pydantic", PydanticBook.parse_raw, book)

    return result


def dataclass_factory() -> Book:
    factory = Factory()

    parser = factory.parser(Book)

    book = serialize.dataclass_factory()

    result = measurer.time_it("Serialize with dataclass_factory", parser, book)

    return result


def test() -> None:
    pydantic()

    dataclass_factory()

    measurer.visualize()
