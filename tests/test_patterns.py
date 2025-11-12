"""Tests for band name patterns."""

from band_name_generator.patterns import BandNamePattern


def test_pattern_enum_exists() -> None:
    """Test that BandNamePattern enum exists and has values."""
    assert BandNamePattern.ADJECTIVE_NOUN is not None
    assert BandNamePattern.COLOR_NOUN is not None
    assert BandNamePattern.METAL_NOUN is not None


def test_multi_word_patterns() -> None:
    """Test multi_word_patterns returns a list."""
    patterns = BandNamePattern.multi_word_patterns()
    assert isinstance(patterns, list)
    assert len(patterns) > 0
    assert all(isinstance(p, BandNamePattern) for p in patterns)


def test_two_word_patterns() -> None:
    """Test two_word_patterns returns a list."""
    patterns = BandNamePattern.two_word_patterns()
    assert isinstance(patterns, list)
    assert len(patterns) > 0
    assert all(isinstance(p, BandNamePattern) for p in patterns)


def test_two_word_subset_of_multi_word() -> None:
    """Test that two-word patterns are subset of multi-word."""
    two_word = set(BandNamePattern.two_word_patterns())
    multi_word = set(BandNamePattern.multi_word_patterns())
    assert two_word.issubset(multi_word)
