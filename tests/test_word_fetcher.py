"""Tests for word fetcher module."""

from band_name_generator.word_fetcher import WordFetcher


def test_word_fetcher_initialization() -> None:
    """Test WordFetcher can be initialized."""
    fetcher = WordFetcher()
    assert fetcher is not None


def test_get_adjective() -> None:
    """Test getting a random adjective."""
    fetcher = WordFetcher()
    adj = fetcher.get_adjective()
    assert isinstance(adj, str)
    assert len(adj) > 0


def test_get_noun() -> None:
    """Test getting a random noun."""
    fetcher = WordFetcher()
    noun = fetcher.get_noun()
    assert isinstance(noun, str)
    assert len(noun) > 0


def test_get_verb() -> None:
    """Test getting a random verb."""
    fetcher = WordFetcher()
    verb = fetcher.get_verb()
    assert isinstance(verb, str)
    assert len(verb) > 0


def test_get_color() -> None:
    """Test getting a random color."""
    fetcher = WordFetcher()
    color = fetcher.get_color()
    assert isinstance(color, str)
    assert len(color) > 0


def test_get_metal() -> None:
    """Test getting a random metal."""
    fetcher = WordFetcher()
    metal = fetcher.get_metal()
    assert isinstance(metal, str)
    assert len(metal) > 0


def test_get_words_single() -> None:
    """Test getting a single random word."""
    fetcher = WordFetcher()
    words = fetcher.get_words(count=1)
    assert len(words) == 1
    assert isinstance(words[0], str)


def test_get_words_multiple() -> None:
    """Test getting multiple random words."""
    fetcher = WordFetcher()
    words = fetcher.get_words(count=5)
    assert len(words) == 5
    assert all(isinstance(word, str) for word in words)
