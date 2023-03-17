import math
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from search.index import Index


class Rank(ABC):
    @abstractmethod
    def score(self, tokens: list[str]) -> dict[int, float]:
        pass


class Bm25(Rank):
    # TODO: add bm25 rank algorithm
    def score(self, tokens: list[str]) -> dict[int, float]:
        raise NotImplementedError("Not implemented")


class TfIdf(Rank):
    def __init__(self, index: "Index"):
        self.index = index

    def __tf(self, doc_id: int, term: str) -> float:
        term_count = self.index.inverted_index[term][doc_id]
        total_count = self.index.tokens_freq[doc_id]

        return term_count / total_count if total_count else 0

    def __idf(self, term: str) -> float:
        if not term in self.index.inverted_index:
            return 0

        return math.log(
            len(self.index.tokens_freq.keys()) / len(self.index.inverted_index[term])
        )

    def __tf_idf(self, doc_id: int, term: str) -> float:
        return self.__tf(doc_id, term) * self.__idf(term)

    def score(self, tokens: list[str]) -> dict[int, float]:
        scores = defaultdict(float)

        for token in tokens:
            for doc_id in self.index.inverted_index.get(token, []):
                score = self.__tf_idf(doc_id, token)

                if score > 0:
                    scores[doc_id] += score

        ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
        return ranked_results
