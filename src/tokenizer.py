# src/tokenizer.py
import re
from typing import List

_TOKEN_RX = re.compile(r"\w+|[^\w\s]", re.UNICODE)


class SimpleTokenizer:
    """Tokenizer muy simple: letras/números y cada signo como token aparte."""

    def __init__(self) -> None:
        self._vocab: dict[str, int] = {}
        self._inv: list[str] = []

    def _id(self, token: str) -> int:
        if token not in self._vocab:
            idx = len(self._vocab)
            self._vocab[token] = idx
            self._inv.append(token)
        return self._vocab[token]

    def encode(self, text: str) -> List[int]:
        tokens = _TOKEN_RX.findall(text.lower())
        return [self._id(t) for t in tokens]

    def decode(self, ids: List[int]) -> str:
        return " ".join(self._inv[i] for i in ids)
