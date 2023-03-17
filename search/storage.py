from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union


@dataclass
class Doc:
    doc_id: int
    doc: any


class Storage(ABC):
    @abstractmethod
    def add(self, doc_id: str, doc: any) -> None:
        pass

    @abstractmethod
    def get(self, doc_id: str) -> Union[Doc, None]:
        pass


class MemoryStorage(Storage):
    def __init__(self):
        self.storage = {}

    def add(self, doc_id: str, doc: any) -> None:
        doc = {**doc, "id": doc_id}
        self.storage[doc_id] = Doc(doc_id=doc_id, doc=doc)

    def get(self, doc_id: str) -> Union[Doc, None]:
        return self.storage[doc_id]
