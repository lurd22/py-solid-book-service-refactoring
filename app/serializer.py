import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from .book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({
            "title": book.title,
            "content": book.content
        })


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")

        title = ET.SubElement(root, "title")
        title.text = book.title

        content = ET.SubElement(root, "content")
        content.text = book.content

        return ET.tostring(root, encoding="unicode")


SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def serialize_book(book: Book, serialize_type: str) -> str:
    if serialize_type not in SERIALIZERS:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
    return SERIALIZERS[serialize_type].serialize(book)
