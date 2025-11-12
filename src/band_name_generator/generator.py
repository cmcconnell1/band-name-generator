"""Main band name generator logic."""

import random

from .patterns import BandNamePattern
from .word_fetcher import WordFetcher


class BandNameGenerator:
    """
    Generate random band names using various patterns.

    This class implements multiple band name generation patterns inspired by
    famous bands like Iron Maiden (metal+noun), The Rolling Stones (the+verb+noun),
    and Black Sabbath (color+noun).

    Attributes:
        word_fetcher: WordFetcher instance used to retrieve random words.

    Example:
        >>> generator = BandNameGenerator()
        >>> names = generator.generate(count=5)
        >>> len(names)
        5
    """

    def __init__(self) -> None:
        """
        Initialize the band name generator.

        Creates a WordFetcher instance that will be used to retrieve
        random words for all name generation methods.
        """
        self.word_fetcher = WordFetcher()

    def _capitalize_band_name(self, name: str) -> str:
        """
        Capitalize each word in the band name.

        Args:
            name: The band name to capitalize (e.g., "iron maiden").

        Returns:
            Band name with each word capitalized (e.g., "Iron Maiden").

        Example:
            >>> generator._capitalize_band_name("dark storm")
            'Dark Storm'
        """
        return " ".join(word.capitalize() for word in name.split())

    def _pluralize(self, word: str) -> str:
        """
        Simple pluralization (not perfect, but good enough).

        Handles common pluralization rules:
        - Words ending in s, x, z, ch, sh → add "es"
        - Words ending in consonant + y → change y to "ies"
        - All other words → add "s"

        Args:
            word: The word to pluralize.

        Returns:
            Pluralized form of the word.

        Examples:
            >>> generator._pluralize("storm")
            'storms'
            >>> generator._pluralize("box")
            'boxes'
            >>> generator._pluralize("city")
            'cities'
        """
        if word.endswith(("s", "x", "z", "ch", "sh")):
            # Words ending in sibilants need "es"
            return word + "es"
        elif word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
            # Consonant + y → ies
            return word[:-1] + "ies"
        else:
            # Default: add "s"
            return word + "s"

    def generate_adjective_noun(self) -> str:
        """Generate a two-word band name: Adjective + Noun.

        Creates names in the style of bands like "Silent Thunder" or "Dark Storm".
        Fetches a random adjective and noun, then capitalizes each word.

        Returns:
            Capitalized band name (e.g., "Electric Mountain", "Broken Wolf").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_adjective_noun()
            >>> len(name.split())
            2
        """
        # Get random adjective and noun from word fetcher
        adj = self.word_fetcher.get_adjective()
        noun = self.word_fetcher.get_noun()
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{adj} {noun}")

    def generate_color_noun(self) -> str:
        """Generate a two-word band name: Color + Noun.

        Creates names in the style of bands like "Black Sabbath", "Black Mountain",
        or "Red River". Fetches a random color and noun.

        Returns:
            Capitalized band name (e.g., "Crimson Wolf", "Azure Dragon").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_color_noun()
            >>> len(name.split())
            2
        """
        # Get random color and noun from word fetcher
        color = self.word_fetcher.get_color()
        noun = self.word_fetcher.get_noun()
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{color} {noun}")

    def generate_metal_noun(self) -> str:
        """Generate a two-word band name: Metal + Noun.

        Creates names in the style of bands like "Iron Maiden" or "Steel Panther".
        Fetches a random metal and noun.

        Returns:
            Capitalized band name (e.g., "Titanium Thunder", "Bronze Wolf").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_metal_noun()
            >>> len(name.split())
            2
        """
        # Get random metal and noun from word fetcher
        metal = self.word_fetcher.get_metal()
        noun = self.word_fetcher.get_noun()
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{metal} {noun}")

    def generate_verb_noun(self) -> str:
        """Generate a two-word band name: Verb + Noun.

        Creates names in the style of bands like "Burning Sky" or "Rolling Thunder".
        Uses present participle verbs (usually ending in -ing).

        Returns:
            Capitalized band name (e.g., "Flying Dragon", "Screaming Eagle").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_verb_noun()
            >>> len(name.split())
            2
        """
        # Get random verb (usually -ing form) and noun from word fetcher
        verb = self.word_fetcher.get_verb()
        noun = self.word_fetcher.get_noun()
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{verb} {noun}")

    def generate_noun_noun(self) -> str:
        """Generate a two-word band name: Noun + Noun.

        Creates names by combining two nouns, like "Thunder Mountain" or
        "Storm Eagle". Both nouns are randomly selected.

        Returns:
            Capitalized band name (e.g., "Fire Dragon", "Ice Wolf").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_noun_noun()
            >>> len(name.split())
            2
        """
        # Get two random nouns from word fetcher
        noun1 = self.word_fetcher.get_noun()
        noun2 = self.word_fetcher.get_noun()
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{noun1} {noun2}")

    def generate_the_adjective_noun(self) -> str:
        """Generate a three-word band name: The + Adjective + Noun (plural).

        Creates names in the style of "The Rolling Stones" or "The Black Keys".
        The noun is pluralized to match the common pattern.

        Returns:
            Capitalized band name starting with "The" (e.g., "The Crystal Roses").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_the_adjective_noun()
            >>> name.startswith("The ")
            True
        """
        # Get random adjective and noun, pluralize the noun
        adj = self.word_fetcher.get_adjective()
        noun = self._pluralize(self.word_fetcher.get_noun())
        # Combine with "the" prefix and capitalize each word
        return self._capitalize_band_name(f"the {adj} {noun}")

    def generate_adjective_adjective_noun(self) -> str:
        """Generate a three-word band name: Adjective + Adjective + Noun.

        Creates names with two adjectives modifying a noun, like "Deep Purple Haze".
        Both adjectives are randomly and independently selected.

        Returns:
            Capitalized band name (e.g., "Dark Silent Thunder", "Electric Crimson Dragon").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_adjective_adjective_noun()
            >>> len(name.split())
            3
        """
        # Get two random adjectives and one noun from word fetcher
        adj1 = self.word_fetcher.get_adjective()
        adj2 = self.word_fetcher.get_adjective()
        noun = self.word_fetcher.get_noun()
        # Combine all three and capitalize each word
        return self._capitalize_band_name(f"{adj1} {adj2} {noun}")

    def generate_adjective_noun_plural(self) -> str:
        """Generate a two-word band name: Adjective + Noun (plural).

        Creates simple two-word names with a plural noun, like "Silent Storms"
        or "Heavy Wizards". The noun is pluralized.

        Returns:
            Capitalized band name with plural noun (e.g., "Silent Storms", "Electric Dragons").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_adjective_noun_plural()
            >>> len(name.split())
            2
        """
        # Get random adjective and noun, pluralize the noun
        adj = self.word_fetcher.get_adjective()
        noun = self._pluralize(self.word_fetcher.get_noun())
        # Combine and capitalize each word
        return self._capitalize_band_name(f"{adj} {noun}")

    def generate_adjective_adjective_noun_plural(self) -> str:
        """Generate a four-word band name: Adjective + Adjective + Noun + Noun (plural).

        Creates names with two adjectives and compound nouns, like
        "Deep Purple Mystic Dragons" or "Atomic Golden Thunder Wizards".

        Returns:
            Capitalized band name with 4 words (e.g., "Deep Purple Mystic Dragons",
            "Dark Silent Thunder Storms", "Atomic Golden Thunder Wizards").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_adjective_adjective_noun_plural()
            >>> len(name.split())
            4
        """
        # Get two random adjectives and two nouns, pluralize the second noun
        adj1 = self.word_fetcher.get_adjective()
        adj2 = self.word_fetcher.get_adjective()
        noun1 = self.word_fetcher.get_noun()
        noun2 = self._pluralize(self.word_fetcher.get_noun())
        # Combine all four words and capitalize each
        return self._capitalize_band_name(f"{adj1} {adj2} {noun1} {noun2}")

    def generate_color_adjective_noun_plural(self) -> str:
        """Generate a four-word band name: Color + Adjective + Noun + Noun (plural).

        Creates names in the style of "Red Hot Chili Peppers".
        Uses a color, an adjective, a singular noun, and a pluralized noun.

        Returns:
            Capitalized band name with 4 words (e.g., "Red Hot Chili Peppers",
            "Blue Electric Thunder Storms", "Black Silent Dragon Warriors").

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_color_adjective_noun_plural()
            >>> len(name.split())
            4
        """
        # Get color, adjective, and two nouns, pluralize the second noun
        color = self.word_fetcher.get_color()
        adj = self.word_fetcher.get_adjective()
        noun1 = self.word_fetcher.get_noun()
        noun2 = self._pluralize(self.word_fetcher.get_noun())
        # Combine all four words and capitalize each
        return self._capitalize_band_name(f"{color} {adj} {noun1} {noun2}")

    def generate_by_pattern(self, pattern: BandNamePattern) -> str:
        """Generate a band name using a specific pattern.

        Maps a BandNamePattern enum value to its corresponding generator method
        and calls it to produce a band name. This is the internal dispatch method
        used by generate().

        Args:
            pattern: The BandNamePattern enum value specifying which pattern to use.

        Returns:
            Generated band name string, capitalized and formatted.

        Raises:
            NotImplementedError: If the specified pattern has no corresponding
                generator method (e.g., COMPOUND_WORD or SINGLE_WORD).

        Example:
            >>> generator = BandNameGenerator()
            >>> name = generator.generate_by_pattern(BandNamePattern.METAL_NOUN)
            >>> isinstance(name, str)
            True
        """
        # Map each pattern enum to its corresponding generator method
        pattern_map = {
            BandNamePattern.ADJECTIVE_NOUN: self.generate_adjective_noun,
            BandNamePattern.COLOR_NOUN: self.generate_color_noun,
            BandNamePattern.METAL_NOUN: self.generate_metal_noun,
            BandNamePattern.VERB_NOUN: self.generate_verb_noun,
            BandNamePattern.NOUN_NOUN: self.generate_noun_noun,
            BandNamePattern.THE_ADJECTIVE_NOUN: self.generate_the_adjective_noun,
            BandNamePattern.ADJECTIVE_ADJECTIVE_NOUN: self.generate_adjective_adjective_noun,
            BandNamePattern.ADJECTIVE_NOUN_PLURAL: self.generate_adjective_noun_plural,
            BandNamePattern.ADJECTIVE_ADJECTIVE_NOUN_PLURAL: (
                self.generate_adjective_adjective_noun_plural
            ),
            BandNamePattern.COLOR_ADJECTIVE_NOUN_PLURAL: (
                self.generate_color_adjective_noun_plural
            ),
        }

        # Look up the generator function for this pattern
        generator_func = pattern_map.get(pattern)
        if generator_func is None:
            # Pattern exists but has no implementation yet
            msg = f"Pattern {pattern} not yet implemented"
            raise NotImplementedError(msg)

        # Call the generator function and return the result
        return generator_func()

    def generate(self, pattern: BandNamePattern | None = None, count: int = 1) -> list[str]:
        """Generate one or more random band names.

        This is the main public API method for generating band names. It can
        generate names using a specific pattern or choose randomly from all
        available patterns.

        Args:
            pattern: Optional BandNamePattern to use. If None, randomly selects
                from all available multi-word patterns for each name generated.
            count: Number of band names to generate. Must be >= 1. Default is 1.

        Returns:
            List of generated band name strings. Each name is properly capitalized.
            Length of list equals the count parameter.

        Example:
            >>> generator = BandNameGenerator()
            >>> names = generator.generate(count=3)
            >>> len(names)
            3
            >>> names = generator.generate(pattern=BandNamePattern.METAL_NOUN, count=2)
            >>> len(names)
            2
        """
        results = []
        # Generate the requested number of names
        for _ in range(count):
            if pattern is None:
                # No pattern specified: choose randomly from all multi-word patterns
                chosen_pattern = random.choice(BandNamePattern.multi_word_patterns())
            else:
                # Use the specified pattern for all generated names
                chosen_pattern = pattern

            # Generate one name using the chosen pattern and add to results
            results.append(self.generate_by_pattern(chosen_pattern))

        return results
