"""Band name patterns and styles.

This module defines the various patterns used to generate band names,
inspired by famous bands like Iron Maiden, The Rolling Stones, and
Black Sabbath.
"""

from enum import Enum


class BandNamePattern(Enum):
    """Enumeration of different patterns for generating band names.

    Each pattern represents a specific word combination style used by
    famous bands. The patterns are categorized into two-word and multi-word
    patterns.

    Attributes:
        ADJECTIVE_NOUN: Two-word pattern combining an adjective and noun.
            Examples: Dark Storm, Silent Thunder
        COLOR_NOUN: Two-word pattern combining a color and noun.
            Examples: Red River, Black Mountain, Black Sabbath
        METAL_NOUN: Two-word pattern combining a metal and noun.
            Examples: Iron Maiden, Steel Panther
        VERB_NOUN: Two-word pattern combining a verb (usually -ing form) and noun.
            Examples: Burning Sky, Rolling Thunder
        NOUN_NOUN: Two-word pattern combining two nouns.
            Examples: Thunder Mountain, Storm Eagle
        THE_ADJECTIVE_NOUN: Three-word pattern with "The" + adjective + plural noun.
            Examples: The Rolling Stones, The Black Keys
        ADJECTIVE_ADJECTIVE_NOUN: Three-word pattern with two adjectives and a noun.
            Examples: Deep Purple Haze
        ADJECTIVE_NOUN_PLURAL: Two-word pattern with adjective + plural noun.
            Examples: Silent Storms, Heavy Wizards
        ADJECTIVE_ADJECTIVE_NOUN_PLURAL: Four-word pattern with two adjectives + noun + plural noun.
            Examples: Deep Purple Mystic Dragons, Atomic Golden Thunder Wizards
        COLOR_ADJECTIVE_NOUN_PLURAL: Four-word pattern with color + adjective + noun + plural noun.
            Examples: Red Hot Chili Peppers, Blue Electric Thunder Storms
        COMPOUND_WORD: Compound or portmanteau words (not yet implemented).
            Examples: Depeche Mode (French compound)
        SINGLE_WORD: Single compound words (not yet implemented).
            Examples: Metallica, Radiohead

    Example:
        >>> pattern = BandNamePattern.METAL_NOUN
        >>> pattern.value
        'metal_noun'
        >>> patterns = BandNamePattern.two_word_patterns()
        >>> len(patterns)
        5
    """

    # Two-word patterns
    ADJECTIVE_NOUN = "adjective_noun"  # Dark Storm, Silent Thunder
    COLOR_NOUN = "color_noun"  # Red River, Black Mountain
    METAL_NOUN = "metal_noun"  # Iron Maiden, Steel Panther
    VERB_NOUN = "verb_noun"  # Burning Sky, Rolling Thunder
    NOUN_NOUN = "noun_noun"  # Thunder Mountain, Storm Eagle

    # Three-word patterns
    THE_ADJECTIVE_NOUN = "the_adjective_noun"  # The Rolling Stones
    ADJECTIVE_ADJECTIVE_NOUN = "adjective_adjective_noun"  # Deep Purple Haze
    ADJECTIVE_NOUN_PLURAL = "adjective_noun_plural"  # Silent Storms (2 words)

    # Four-word patterns
    ADJECTIVE_ADJECTIVE_NOUN_PLURAL = "adjective_adjective_noun_plural"  # Deep Purple Mystic Dragons
    COLOR_ADJECTIVE_NOUN_PLURAL = "color_adjective_noun_plural"  # Red Hot Chili Peppers

    # Compound/portmanteau patterns (not yet implemented)
    COMPOUND_WORD = "compound_word"  # Depeche Mode (French compound)
    SINGLE_WORD = "single_word"  # Metallica, Radiohead

    @classmethod
    def multi_word_patterns(cls) -> list["BandNamePattern"]:
        """Get all patterns that generate multi-word band names.

        Returns all currently implemented patterns that produce band names
        with multiple words. This excludes COMPOUND_WORD and SINGLE_WORD
        which are not yet implemented.

        Returns:
            List of BandNamePattern enum values for multi-word patterns.
            Currently returns 10 patterns (6 two-word + 4 multi-word).

        Example:
            >>> patterns = BandNamePattern.multi_word_patterns()
            >>> len(patterns)
            10
            >>> BandNamePattern.METAL_NOUN in patterns
            True
        """
        return [
            cls.ADJECTIVE_NOUN,
            cls.COLOR_NOUN,
            cls.METAL_NOUN,
            cls.VERB_NOUN,
            cls.NOUN_NOUN,
            cls.THE_ADJECTIVE_NOUN,
            cls.ADJECTIVE_ADJECTIVE_NOUN,
            cls.ADJECTIVE_NOUN_PLURAL,
            cls.ADJECTIVE_ADJECTIVE_NOUN_PLURAL,
            cls.COLOR_ADJECTIVE_NOUN_PLURAL,
        ]

    @classmethod
    def two_word_patterns(cls) -> list["BandNamePattern"]:
        """Get patterns that generate exactly two-word band names.

        Returns only the patterns that produce names with exactly two words.
        This is a subset of multi_word_patterns().

        Returns:
            List of BandNamePattern enum values for two-word patterns.
            Currently returns 6 patterns.

        Example:
            >>> patterns = BandNamePattern.two_word_patterns()
            >>> len(patterns)
            6
            >>> BandNamePattern.ADJECTIVE_NOUN in patterns
            True
            >>> BandNamePattern.THE_ADJECTIVE_NOUN in patterns
            False
        """
        return [
            cls.ADJECTIVE_NOUN,
            cls.COLOR_NOUN,
            cls.METAL_NOUN,
            cls.VERB_NOUN,
            cls.NOUN_NOUN,
            cls.ADJECTIVE_NOUN_PLURAL,
        ]
