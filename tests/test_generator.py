"""Tests for band name generator."""

from band_name_generator.generator import BandNameGenerator
from band_name_generator.patterns import BandNamePattern


def test_generator_initialization() -> None:
    """Test BandNameGenerator can be initialized."""
    generator = BandNameGenerator()
    assert generator is not None


def test_generate_adjective_noun() -> None:
    """Test generating adjective + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_adjective_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 2
    # Should be title case
    words = name.split()
    assert all(word[0].isupper() for word in words)


def test_generate_color_noun() -> None:
    """Test generating color + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_color_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 2


def test_generate_metal_noun() -> None:
    """Test generating metal + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_metal_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 2


def test_generate_verb_noun() -> None:
    """Test generating verb + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_verb_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 2


def test_generate_noun_noun() -> None:
    """Test generating noun + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_noun_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 2


def test_generate_the_adjective_noun() -> None:
    """Test generating 'the' + adjective + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_the_adjective_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 3
    assert name.split()[0].lower() == "the"


def test_generate_adjective_adjective_noun() -> None:
    """Test generating adjective + adjective + noun pattern."""
    generator = BandNameGenerator()
    name = generator.generate_adjective_adjective_noun()
    assert isinstance(name, str)
    assert len(name.split()) == 3


def test_generate_adjective_noun_plural() -> None:
    """Test generating adjective + noun (plural) pattern."""
    generator = BandNameGenerator()
    name = generator.generate_adjective_noun_plural()
    assert isinstance(name, str)
    assert len(name.split()) == 2


def test_generate_adjective_adjective_noun_plural() -> None:
    """Test generating adjective + adjective + noun + noun (plural) pattern."""
    generator = BandNameGenerator()
    name = generator.generate_adjective_adjective_noun_plural()
    assert isinstance(name, str)
    assert len(name.split()) == 4
    # Last word should be plural (end in s/es/ies)
    last_word = name.split()[-1].lower()
    assert last_word.endswith(("s", "es", "ies"))


def test_generate_color_adjective_noun_plural() -> None:
    """Test generating color + adjective + noun + noun (plural) pattern."""
    generator = BandNameGenerator()
    name = generator.generate_color_adjective_noun_plural()
    assert isinstance(name, str)
    assert len(name.split()) == 4
    # Last word should be plural (end in s/es/ies)
    last_word = name.split()[-1].lower()
    assert last_word.endswith(("s", "es", "ies"))


def test_generate_by_pattern() -> None:
    """Test generating with specific pattern."""
    generator = BandNameGenerator()
    name = generator.generate_by_pattern(BandNamePattern.METAL_NOUN)
    assert isinstance(name, str)
    assert len(name) > 0


def test_generate_single() -> None:
    """Test generating a single band name."""
    generator = BandNameGenerator()
    names = generator.generate(count=1)
    assert len(names) == 1
    assert isinstance(names[0], str)


def test_generate_multiple() -> None:
    """Test generating multiple band names."""
    generator = BandNameGenerator()
    names = generator.generate(count=5)
    assert len(names) == 5
    assert all(isinstance(name, str) for name in names)


def test_generate_with_pattern() -> None:
    """Test generating with specific pattern."""
    generator = BandNameGenerator()
    names = generator.generate(pattern=BandNamePattern.COLOR_NOUN, count=3)
    assert len(names) == 3
    assert all(isinstance(name, str) for name in names)


def test_pluralize_simple() -> None:
    """Test simple pluralization."""
    generator = BandNameGenerator()
    assert generator._pluralize("cat") == "cats"
    assert generator._pluralize("dog") == "dogs"


def test_pluralize_special_endings() -> None:
    """Test pluralization with special endings."""
    generator = BandNameGenerator()
    assert generator._pluralize("box") == "boxes"
    assert generator._pluralize("church") == "churches"
    assert generator._pluralize("city") == "cities"
