# Band Name Generator

Generate random band names in the style of famous bands like Iron Maiden, Red Hot Chili Peppers, The Rolling Stones, and more.

## Features

- 10 different name patterns (2-word, 3-word, and 4-word combinations)
- Continuous random mode with configurable intervals
- CLI with pattern selection
- 32 tests with 97% coverage
- Full type hints with mypy
- Modern Python development using uv

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd band-name-generator

# Install dependencies with uv (https://github.com/astral-sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

## Quick Start

```bash
# Generate a single random band name
uv run python -m band_name_generator

# Generate 10 random names
uv run python -m band_name_generator -n 10

# List all available patterns
uv run python -m band_name_generator -l

# Generate names with specific patterns
uv run python -m band_name_generator -p metal_noun -n 5                  # Iron Maiden style
uv run python -m band_name_generator -p color_noun -n 5                  # Black Sabbath style
uv run python -m band_name_generator -p the_adjective_noun -n 5          # The Rolling Stones style
uv run python -m band_name_generator -p color_adjective_noun_plural -n 5 # Red Hot Chili Peppers style

# Continuous random mode (generates names every 5 seconds)
uv run python -m band_name_generator --random

# Custom interval (2 seconds between names)
uv run python -m band_name_generator --random --interval 2

# Generate 10 names in random mode then stop
uv run python -m band_name_generator --random -n 10

# Test random mode with timeout (useful for testing)
timeout 12 uv run python -m band_name_generator --random --interval 2 -n 3

# Enable verbose mode to see word source debug info
uv run python -m band_name_generator -v -n 5
```

## Available Patterns

The generator includes 10 different patterns:

**Two-word patterns:**
- `adjective_noun` - Dark Storm, Silent Thunder
- `color_noun` - Red River, Black Mountain
- `metal_noun` - Iron Maiden, Steel Panther
- `verb_noun` - Burning Sky, Rolling Thunder
- `noun_noun` - Thunder Mountain, Storm Eagle
- `adjective_noun_plural` - Silent Storms, Heavy Wizards

**Three-word patterns:**
- `the_adjective_noun` - The Rolling Stones, The Black Keys
- `adjective_adjective_noun` - Deep Purple Haze

**Four-word patterns:**
- `color_adjective_noun_plural` - Red Hot Chili Peppers [RECOMMENDED]
- `adjective_adjective_noun_plural` - Deep Purple Mystic Dragons

## Examples

```bash
# Generate 5 metal-themed band names (like Iron Maiden)
$ uv run python -m band_name_generator -p metal_noun -n 5

Generated 5 band names:
  1. Iron Maiden
  2. Steel Dragon
  3. Bronze Wolf
  4. Titanium Thunder
  5. Chrome Raven

# Generate 5 "The" style names (like The Rolling Stones)
$ uv run python -m band_name_generator -p the_adjective_noun -n 5

Generated 5 band names:
  1. The Rolling Stones
  2. The Sacred Deserts
  3. The Crystal Roses
  4. The Ancient Blades
  5. The Lunar Wizards

# Generate 5 four-word names (like Red Hot Chili Peppers)
$ uv run python -m band_name_generator -p color_adjective_noun_plural -n 5

Generated 5 band names:
  1. Red Hot Chili Peppers
  2. Black Velvet Bear Forests
  3. Blue Electric Thunder Storms
  4. Scarlet Frozen Petal Valleys
  5. Emerald Golden Thorn Serpents

# Continuous random mode with 5-second pauses (Ctrl+C to stop)
$ uv run python -m band_name_generator --random

Random Band Name Generator
Generating names continuously with 5.0s intervals [Press Ctrl+C to stop]

Generated band name:
  Iron Thunder

[5 second pause]

Generated band name:
  The Wild Warriors

[5 second pause]

Generated band name:
  Red Hot Chili Peppers

[continues until Ctrl+C]

# Random mode with custom interval (2 seconds)
$ uv run python -m band_name_generator --random --interval 2

# Generate 10 random names with 5-second pauses then stop
$ uv run python -m band_name_generator --random -n 10

Random Band Name Generator
Generating 10 names with 5.0s intervals [Press Ctrl+C to stop]

Generated band name:
  Steel Dragon

[5 second pause]

Generated band name:
  The Rolling Stones

[5 second pause]
...
Generated 10 names. Exiting.

# Test random mode with timeout command
# Note: timeout value must accommodate (count × interval) seconds
# Example: 3 names × 2 seconds = 6 seconds minimum (use 12 for buffer)
$ timeout 12 uv run python -m band_name_generator --random --interval 2 -n 3

Random Band Name Generator
Generating 3 names with 2.0s intervals [Press Ctrl+C to stop]

Generated band name:
  Rusty Savage Desert

Generated band name:
  The Wild Warriors

Generated band name:
  Burning Rain

Generated 3 names. Exiting.

# For 20 names with 5-second intervals, need 100+ seconds
# (20 names × 5 seconds = 100 seconds minimum)
$ timeout 105 uv run python -m band_name_generator --random --interval 5 -n 20
```

**Timeout Calculation Guide:**
- Formula: `timeout_seconds >= (count × interval) + buffer`
- Example: 20 names × 5 seconds = 100 seconds minimum (use 105-120 for safety)
- Example: 3 names × 2 seconds = 6 seconds minimum (use 12 for safety)

## Verbose/Debug Mode

Use the `-v` or `--verbose` flag to see debug information about word fetching:

```bash
# Enable verbose mode to see word source details
$ uv run python -m band_name_generator -v -n 2

[DEBUG] WordFetcher initialized
[DEBUG] Built-in word lists: 32 adjectives, 48 nouns, 13 verbs, 16 colors, 12 metals
[DEBUG] Category methods (get_adjective, get_noun, etc.) use built-in lists
[DEBUG] get_words() method can fetch from remote source: https://www.mit.edu/~ecprice/wordlist.10000

Generated 2 band names:
  1. Bronze Root
  2. Electric Heavy Storm
```

**What verbose mode shows:**
- Built-in word list sizes (adjectives, nouns, verbs, colors, metals)
- Which word sources are being used
- Remote fetch attempts and results (if using `get_words()` method)
- Fallback behavior when remote fetching fails

**Note:** The band name generator currently uses built-in curated word lists for all patterns. Remote word fetching is available via the `get_words()` API method but not currently used by the pattern generators.

## Documentation

- [BAND-NAME-GENERATOR.md](docs/BAND-NAME-GENERATOR.md) - Complete documentation with all pattern examples
- [UV-RUST-STANDARD.md](docs/UV-RUST-STANDARD.md) - Python development standards and boilerplate templates

## Development

This project uses modern Python development tools:

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type check
uv run mypy src/

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov
```

## Project Structure

```
band-name-generator/
├── src/band_name_generator/  # Source code
│   ├── cli.py                 # Command-line interface
│   ├── generator.py           # Main generator logic
│   ├── patterns.py            # Pattern definitions
│   └── word_fetcher.py        # Word fetching utilities
├── tests/                     # Test suite (97% coverage)
├── docs/                      # Documentation
├── scripts/                   # Setup scripts (for boilerplate reference)
└── templates/                 # Python project templates (for boilerplate reference)
```

## Technologies

- Python 3.14+
- uv (Rust-based package manager)
- pytest (testing)
- ruff (linting and formatting)
- mypy (type checking)

## Boilerplate Templates

This repository also includes production-ready Python project templates demonstrating modern development practices. See [UV-RUST-STANDARD.md](docs/UV-RUST-STANDARD.md) for details on using these templates for other projects.

## Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)

## License

This project is provided as-is for educational and entertainment purposes.

---

**Version:** 1.0
**Last Updated:** 2025-11-12
