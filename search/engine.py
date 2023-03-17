from search.index import Index
from search.rank import TfIdf


class Engine:
    def __init__(self, index: Index = Index()):
        self.__index: Index = index

    def index(self, doc_id: str, obj: dict) -> None:
        self.__index.add(doc_id, obj)

    def search(self, query: str, **kwargs) -> list[dict]:
        rank_function = kwargs["rank_function"] if "rank_function" in kwargs else TfIdf
        return self.__index.search(query, rank_function=rank_function)
