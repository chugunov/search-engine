import string
from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    def tokenize(self, obj: object) -> list[str]:
        pass


class SimpleTokenizer(Tokenizer):
    def __init__(self):
        self.__stop_words = list(string.punctuation)

    def __tokenize(self, text: str) -> list[str]:
        tokens = []
        for token in text.lower().split():
            if not token in self.__stop_words:
                tokens.append(token)
        return tokens

    def tokenize(self, obj: object) -> list[str]:
        tokens = []
        if isinstance(obj, str):
            tokens += self.__tokenize(obj)
        elif isinstance(obj, dict):
            for k in obj:
                tokens += self.tokenize(obj[k])
        return tokens
