from collections import defaultdict


from search.rank import Rank
from search.nested_dict import NestedDict
from search.tokenizer import Tokenizer, SimpleTokenizer
from search.storage import Storage, MemoryStorage


class Index:
    def __init__(
        self,
        tokenizer: Tokenizer = SimpleTokenizer,
        storage: Storage = MemoryStorage,
    ):
        self.storage: Storage = storage()
        self.tokenizer: Tokenizer = tokenizer()
        self.tokens_freq = defaultdict(int)
        self.inverted_index = NestedDict()

    def add(self, doc_id: str, obj: object) -> None:
        tokens = self.tokenizer.tokenize(obj)
        for token in tokens:
            if not self.inverted_index.get(token, {}).get(doc_id) is None:
                continue
            self.inverted_index[token][doc_id] += tokens.count(token)
        self.tokens_freq[doc_id] = len(tokens)

        self.storage.add(doc_id=doc_id, doc=obj)

    def search(self, query, rank_function: Rank) -> dict:
        query_tokens = self.tokenizer.tokenize(query)
        ranked_result = rank_function(self).score(query_tokens)
        for doc_id, score in ranked_result:
            yield {"id": doc_id, "doc": self.storage.get(doc_id).doc, "score": score}
