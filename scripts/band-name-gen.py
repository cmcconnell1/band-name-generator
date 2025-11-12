import random

# Try to import the preferred library package first
try:
    from random_word import RandomWords

    PACKAGE_AVAILABLE = True
except ImportError:
    PACKAGE_AVAILABLE = False

# Import requests library for the fallback method
try:
    import requests

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

# Fallback Word List URL (a large list of common words)
WORD_LIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"


def get_word_from_package():
    """Tries to get a random word using the installed package."""
    print("Attempting to get a word from the 'random-word' package...")
    try:
        r = RandomWords()
        # Get a word with a dictionary definition, between 5 and 10 characters long
        word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=10)

        if word:
            return word.lower()
        else:
            print("Package returned an empty or filtered result. Falling back...")
            return None

    except Exception as e:
        print(f"Error using random-word package: {e}. Falling back...")
        return None


def get_word_from_url_fallback():
    """Fetches a word from a public URL word list as a fallback."""
    print(f"Attempting to fetch a word from online URL: {WORD_LIST_URL}")
    try:
        if not REQUESTS_AVAILABLE:
            print("The 'requests' library is not installed for the URL fallback.")
            return None

        response = requests.get(WORD_LIST_URL, timeout=5)  # Added a timeout
        response.raise_for_status()  # Raise exception for bad status codes

        words = response.content.decode("utf-8").splitlines()

        # Simple filter for the URL list
        words = [word.lower() for word in words if 4 <= len(word.strip()) <= 12 and word.isalpha()]

        if words:
            return random.choice(words)
        else:
            print("URL list was empty after filtering.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve word list from URL: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during URL fetch: {e}")
        return None


# --- Main Logic ---


def get_random_dictionary_word():
    """Main function to get a random word, using package first, then URL, then a default list."""

    # 1. Try the dedicated package (Preferred method)
    if PACKAGE_AVAILABLE:
        word = get_word_from_package()
        if word:
            return word

    # 2. Try the URL fallback
    if REQUESTS_AVAILABLE:
        word = get_word_from_url_fallback()
        if word:
            return word

    # 3. Final Default Fallback (no internet or no libs)
    print("Using local default words as a final fallback.")
    default_words = ["algorithm", "script", "terminal", "module", "execute", "python", "variable"]
    return random.choice(default_words)


# Execute and use the random word
random_word = get_random_dictionary_word()

print("\n--- Result ---")
print(f"Successfully generated a random word: **{random_word.upper()}**")
print("--------------")

# Example of how you can use the word in your script logic
if len(random_word) > 7:
    print("This is a long word!")
else:
    print("This is a concise word.")
