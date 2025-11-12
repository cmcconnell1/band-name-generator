"""Utilities for fetching random words from various sources."""

import random

try:
    import requests

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


# Word list sources
WORD_LIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"

# Fallback word lists by category
ADJECTIVES = [
    "broken",
    "electric",
    "burning",
    "frozen",
    "wild",
    "dark",
    "silent",
    "crimson",
    "golden",
    "iron",
    "steel",
    "velvet",
    "crystal",
    "neon",
    "atomic",
    "cosmic",
    "lunar",
    "solar",
    "mystic",
    "savage",
    "ancient",
    "modern",
    "twisted",
    "sacred",
    "dirty",
    "clean",
    "rusty",
    "shiny",
    "heavy",
    "light",
    "deep",
    "shallow",
]

NOUNS = [
    "storm",
    "thunder",
    "lightning",
    "fire",
    "ice",
    "wind",
    "rain",
    "snow",
    "mountain",
    "valley",
    "ocean",
    "river",
    "forest",
    "desert",
    "city",
    "street",
    "machine",
    "engine",
    "weapon",
    "tool",
    "hammer",
    "blade",
    "sword",
    "shield",
    "wolf",
    "bear",
    "tiger",
    "eagle",
    "dragon",
    "phoenix",
    "serpent",
    "raven",
    "maiden",
    "warrior",
    "priest",
    "wizard",
    "prophet",
    "king",
    "queen",
    "knight",
    "rose",
    "thorn",
    "petal",
    "seed",
    "root",
    "vine",
    "tree",
    "leaf",
]

COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "black",
    "white",
    "silver",
    "gold",
    "crimson",
    "scarlet",
    "azure",
    "emerald",
    "amber",
    "violet",
    "indigo",
]

METALS = [
    "iron",
    "steel",
    "bronze",
    "copper",
    "silver",
    "gold",
    "platinum",
    "titanium",
    "chrome",
    "aluminum",
    "zinc",
    "tin",
]

VERBS = [
    "burning",
    "rising",
    "falling",
    "flying",
    "running",
    "screaming",
    "crying",
    "bleeding",
    "breaking",
    "melting",
    "freezing",
    "spinning",
    "rolling",
]


class WordFetcher:
    """
    Fetches random words from various sources.

    This class provides methods to get random words from either an online
    word list or built-in fallback lists. Words can be retrieved by category
    (adjectives, nouns, verbs, colors, metals) or as general random words.

    Attributes:
        _cached_words: Optional cache of words fetched from online source.
                      Initialized as None and populated on first use.
    """

    def __init__(self) -> None:
        """
        Initialize the word fetcher.

        Sets up an empty cache for words fetched from online sources.
        The cache will be populated lazily on first use if use_cache=True.
        """
        self._cached_words: list[str] | None = None

    def _fetch_word_list(self) -> list[str]:
        """
        Fetch word list from online source.

        Attempts to download a word list from MIT's public word list URL.
        Filters words to only include those between 4-12 characters that
        contain only alphabetic characters.

        Returns:
            List of filtered words in lowercase, or empty list if fetch fails.

        Note:
            Requires the 'requests' library to be available. Returns empty
            list if requests is not installed or if any network error occurs.
        """
        # Check if requests library is available
        if not REQUESTS_AVAILABLE:
            return []

        try:
            # Fetch word list from MIT with 5 second timeout
            response = requests.get(WORD_LIST_URL, timeout=5)
            response.raise_for_status()  # Raise exception for bad status codes

            # Decode response and split into individual words
            words = response.content.decode("utf-8").splitlines()

            # Filter words: 4-12 characters, alphabetic only, convert to lowercase
            return [
                word.lower() for word in words if 4 <= len(word.strip()) <= 12 and word.isalpha()
            ]
        except Exception:
            # Return empty list on any error (network, timeout, decode, etc.)
            return []

    def get_words(self, count: int = 1, use_cache: bool = True) -> list[str]:
        """
        Get random words from online source or fallback.

        Attempts to fetch random words from an online word list. If that fails,
        falls back to built-in word lists (adjectives, nouns, verbs).

        Args:
            count: Number of words to fetch. Default is 1.
            use_cache: Whether to cache the word list from online source.
                      Default is True. Set to False to always fetch fresh words.

        Returns:
            List of random words. Length will match the count parameter.

        Example:
            >>> fetcher = WordFetcher()
            >>> words = fetcher.get_words(count=3)
            >>> len(words)
            3
        """
        # Populate cache on first use if caching is enabled
        if use_cache and self._cached_words is None:
            self._cached_words = self._fetch_word_list()

        # Use cached words or fetch fresh ones based on use_cache flag
        word_source = self._cached_words if use_cache else self._fetch_word_list()

        # If we successfully got words from online source, use them
        if word_source:
            return [random.choice(word_source) for _ in range(count)]

        # Fallback: combine all built-in word lists and select randomly
        all_words = ADJECTIVES + NOUNS + VERBS
        return [random.choice(all_words) for _ in range(count)]

    def get_adjective(self) -> str:
        """
        Get a random adjective.

        Returns:
            A random adjective from the ADJECTIVES list (e.g., "dark", "electric").
        """
        return random.choice(ADJECTIVES)

    def get_noun(self) -> str:
        """
        Get a random noun.

        Returns:
            A random noun from the NOUNS list (e.g., "storm", "mountain").
        """
        return random.choice(NOUNS)

    def get_verb(self) -> str:
        """
        Get a random verb (usually present participle).

        Returns:
            A random verb from the VERBS list (e.g., "burning", "falling").

        Note:
            Most verbs in the list are present participles (ending in -ing)
            suitable for band name patterns like "Burning Sky".
        """
        return random.choice(VERBS)

    def get_color(self) -> str:
        """
        Get a random color.

        Returns:
            A random color from the COLORS list (e.g., "red", "crimson").
        """
        return random.choice(COLORS)

    def get_metal(self) -> str:
        """
        Get a random metal.

        Returns:
            A random metal from the METALS list (e.g., "iron", "steel").

        Note:
            Used for band names like "Iron Maiden" or "Steel Panther".
        """
        return random.choice(METALS)
