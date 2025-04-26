# tests/test_tokenizer.py
from src.tokenizer import SimpleTokenizer


def test_roundtrip():
    tok = SimpleTokenizer()
    text = "¡Hola, FIEE 2025!"
    ids = tok.encode(text)
    assert isinstance(ids, list)
    decoded = tok.decode(ids)
    # Simplísimo: baja a minúsculas y separa signos con espacios
    assert decoded == "¡ hola , fiee 2025 !".strip()


def test_vocab_grows_as_needed():
    tok = SimpleTokenizer()
    tok.encode("uno dos dos")
    assert len(tok._vocab) == 2
