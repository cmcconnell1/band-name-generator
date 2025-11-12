# Band Name Generator

Generate random band names in the style of famous bands like Depeche Mode, Iron Maiden, Limp Bizkit, and The Rolling Stones.

## Features

- 10 different word patterns (2-word, 3-word, and 4-word combinations)
- Built-in word categories (colors, metals, adjectives, nouns, verbs)
- CLI interface with pattern selection
- Fully typed with type hints
- 97% test coverage
- Uses modern Rust-based uv workflow

## Installation

```bash
# Clone and setup
cd band-name-generator
uv sync

# Or use the modern setup script
./scripts/setup-python-uv-modern.sh
```

## Usage

### Command Line

```bash
# Generate a single random band name
uv run python -m band_name_generator

# Generate multiple names
uv run python -m band_name_generator -n 10

# Use a specific pattern
uv run python -m band_name_generator -p metal_noun -n 5

# List all available patterns
uv run python -m band_name_generator -l

# Random continuous mode (generates names every 5 seconds)
uv run python -m band_name_generator --random

# Random mode with custom interval (3 seconds)
uv run python -m band_name_generator --random --interval 3

# Generate 10 names in random mode then stop
uv run python -m band_name_generator --random -n 10

# Test random mode with timeout (useful for testing)
timeout 12 uv run python -m band_name_generator --random --interval 2 -n 3
```

### Python API

```python
from band_name_generator import BandNameGenerator, BandNamePattern

# Create generator
generator = BandNameGenerator()

# Generate random names
names = generator.generate(count=5)
# ['Electric Storm', 'Iron Maiden', 'Silent Thunder', ...]

# Generate with specific pattern
names = generator.generate(pattern=BandNamePattern.METAL_NOUN, count=3)
# ['Iron Warrior', 'Steel Dragon', 'Titanium Wolf']

# Generate using specific methods
name = generator.generate_adjective_noun()  # 'Dark Mountain'
name = generator.generate_the_adjective_noun()  # 'The Rolling Stones'
```

## Available Patterns

### Two-Word Patterns

- **adjective_noun** - Dark Storm, Silent Thunder
- **color_noun** - Red River, Black Mountain
- **metal_noun** - Iron Maiden, Steel Panther
- **verb_noun** - Burning Sky, Rolling Thunder
- **noun_noun** - Thunder Mountain, Storm Eagle
- **adjective_noun_plural** - Silent Storms, Heavy Wizards

### Multi-Word Patterns (3+ words)

**3-word patterns:**
- **the_adjective_noun** - The Rolling Stones, The Black Keys
- **adjective_adjective_noun** - Deep Purple Haze

**4-word patterns:**
- **color_adjective_noun_plural** - Red Hot Chili Peppers [RECOMMENDED] (Color + Adjective + Noun + Plural)
- **adjective_adjective_noun_plural** - Deep Purple Mystic Dragons (Adjective + Adjective + Noun + Plural)

## CLI Usage Examples

### List All Available Patterns

```bash
# Show all available patterns
$ uv run python -m band_name_generator -l

Available patterns:

Two-word patterns:
  - adjective_noun
  - color_noun
  - metal_noun
  - verb_noun
  - noun_noun
  - adjective_noun_plural

Multi-word patterns:
  - the_adjective_noun
  - adjective_adjective_noun
  - adjective_adjective_noun_plural
  - color_adjective_noun_plural
```

### Two-Word Pattern Examples

#### Adjective + Noun Pattern

Generate names like "Silent Thunder" or "Dark Storm":

```bash
$ uv run python -m band_name_generator -p adjective_noun -n 5

Generated 5 band names:
  1. Electric Mountain
  2. Silent Thunder
  3. Broken Storm
  4. Crimson Wolf
  5. Dark Forest
```

#### Color + Noun Pattern

Generate names like "Black Sabbath" or "Red River":

```bash
$ uv run python -m band_name_generator -p color_noun -n 5

Generated 5 band names:
  1. Black Mountain
  2. Crimson Wolf
  3. Azure Dragon
  4. Emerald Storm
  5. Violet Thunder
```

#### Metal + Noun Pattern

Generate names like "Iron Maiden" or "Steel Panther":

```bash
$ uv run python -m band_name_generator -p metal_noun -n 5

Generated 5 band names:
  1. Iron Maiden
  2. Steel Dragon
  3. Bronze Wolf
  4. Titanium Thunder
  5. Chrome Raven
```

#### Verb + Noun Pattern

Generate names like "Burning Sky" or "Rolling Thunder":

```bash
$ uv run python -m band_name_generator -p verb_noun -n 5

Generated 5 band names:
  1. Burning Sky
  2. Rising Phoenix
  3. Falling Mountain
  4. Screaming Eagle
  5. Flying Dragon
```

#### Noun + Noun Pattern

Generate names like "Thunder Mountain" or "Storm Eagle":

```bash
$ uv run python -m band_name_generator -p noun_noun -n 5

Generated 5 band names:
  1. Thunder Mountain
  2. Storm Eagle
  3. Fire Dragon
  4. Ice Wolf
  5. Lightning Serpent
```

### Multi-Word Pattern Examples

#### The + Adjective + Noun (Plural) Pattern

Generate names like "The Rolling Stones" or "The Black Keys":

```bash
$ uv run python -m band_name_generator -p the_adjective_noun -n 5

Generated 5 band names:
  1. The Rolling Stones
  2. The Sacred Deserts
  3. The Crystal Roses
  4. The Ancient Blades
  5. The Lunar Wizards
```

#### Adjective + Adjective + Noun Pattern

Generate names like "Deep Purple Haze":

```bash
$ uv run python -m band_name_generator -p adjective_adjective_noun -n 5

Generated 5 band names:
  1. Deep Purple Storm
  2. Dark Silent Thunder
  3. Electric Crimson Dragon
  4. Ancient Mystic Wolf
  5. Golden Crystal Phoenix
```

#### Adjective + Noun (Plural) Pattern

Generate simple two-word names with plural nouns:

```bash
$ uv run python -m band_name_generator -p adjective_noun_plural -n 5

Generated 5 band names:
  1. Silent Storms
  2. Electric Dragons
  3. Broken Wolves
  4. Heavy Wizards
  5. Atomic Machines
```

#### Adjective + Adjective + Noun + Noun (Plural) Pattern

Generate 4-word names with two adjectives:

```bash
$ uv run python -m band_name_generator -p adjective_adjective_noun_plural -n 5

Generated 5 band names:
  1. Deep Purple Mystic Dragons
  2. Atomic Golden Thunder Wizards
  3. Dark Savage Hammer Lightnings
  4. Broken Wild Ice Hammers
  5. Electric Crimson Storm Warriors
```

#### Color + Adjective + Noun + Noun (Plural) Pattern

Generate 4-word names like "Red Hot Chili Peppers" [RECOMMENDED for this style]:

```bash
$ uv run python -m band_name_generator -p color_adjective_noun_plural -n 5

Generated 5 band names:
  1. Red Hot Chili Peppers
  2. Black Velvet Bear Forests
  3. Blue Electric Thunder Storms
  4. Scarlet Frozen Petal Valleys
  5. Emerald Golden Thorn Serpents
```

### Random Pattern Generation

Generate names using random patterns (the default behavior):

```bash
# Single random name
$ uv run python -m band_name_generator

Generated band name:
  Iron Thunder

# Multiple random names with mixed patterns
$ uv run python -m band_name_generator -n 15

Generated 15 band names:
  1. Spinning Wizard
  2. Purple Storm
  3. The Solar Snows
  4. Steel Solar Bear
  5. Silent City
  6. Rain Root
  7. Titanium Prophet
  8. Rising Knight
  9. Iron Burning Forest
  10. Broken Blades
  11. Solar Shiny Tree
  12. Scarlet Priest
  13. Freezing Wolf
  14. Ice Queen
  15. Maiden Forest
```

### Continuous Random Mode

Generate names continuously with automatic pauses (perfect for brainstorming):

```bash
# Infinite random mode (press Ctrl+C to stop)
$ uv run python -m band_name_generator --random

Random Band Name Generator
Generating names continuously with 5.0s intervals [Press Ctrl+C to stop]

Generated band name:
  Azure Dark River Winds

[5 second pause]

Generated band name:
  Iron Maiden

[5 second pause]

Generated band name:
  The Rolling Stones

[continues until Ctrl+C]

# Custom interval (3 seconds between names)
$ uv run python -m band_name_generator --random --interval 3

# Generate 10 names then stop
$ uv run python -m band_name_generator --random -n 10

Random Band Name Generator
Generating 10 names with 5.0s intervals [Press Ctrl+C to stop]

Generated band name:
  Silver Clean Machine Machines

[5 second pause]
...
Generated 10 names. Exiting.

# Use specific pattern in random mode
$ uv run python -m band_name_generator --random -p color_adjective_noun_plural --interval 2

# Test with timeout command (useful for testing)
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
```

## Project Structure

```
band-name-generator/
├── src/band_name_generator/
│   ├── __init__.py         # Package exports
│   ├── __main__.py         # CLI entry point
│   ├── cli.py              # Command-line interface
│   ├── generator.py        # Main generator logic
│   ├── patterns.py         # Pattern definitions
│   └── word_fetcher.py     # Word fetching utilities
│
├── tests/                  # Comprehensive tests
│   ├── test_generator.py
│   ├── test_patterns.py
│   └── test_word_fetcher.py
│
├── scripts/                # Setup and utility scripts
├── templates/              # Python project templates
└── docs/                   # Documentation
```

## Development

### Modern UV Workflow - Quick Reference

**NO VENV ACTIVATION NEEDED!** Use `uv run` for everything:

```bash
# Code Quality
uv run ruff format .        # Format code
uv run ruff check .         # Lint code
uv run ruff check --fix .   # Fix issues automatically
uv run mypy src/            # Type check

# Testing
uv run pytest               # Run tests
uv run pytest -v            # Verbose output
uv run pytest --cov         # With coverage report

# Running
uv run python -m band_name_generator           # Run generator
uv run python -m band_name_generator -n 10     # Generate 10 names

# Dependencies
uv add package-name         # Add dependency
uv add --dev package-name   # Add dev dependency
uv sync                     # Sync environment
```

## Test Coverage

```
30 tests passed
97% coverage

Module breakdown:
- generator.py: 97% coverage
- patterns.py: 100% coverage
- word_fetcher.py: 84% coverage
```

## Word Categories

The generator includes built-in word lists:

- **Adjectives**: broken, electric, burning, frozen, wild, dark, silent, crimson...
- **Nouns**: storm, thunder, fire, ice, mountain, wolf, dragon, maiden...
- **Colors**: red, blue, black, white, silver, gold, crimson, violet...
- **Metals**: iron, steel, bronze, silver, gold, titanium, chrome...
- **Verbs**: burning, rising, falling, flying, screaming, breaking...

## Technologies

- **Python 3.14+**
- **uv** (Rust-based package manager)
- **pytest** (testing)
- **ruff** (linting and formatting)
- **mypy** (type checking)

## Modern uv Workflow

This project uses the modern Rust-based uv workflow:

```bash
# Add dependencies
uv add requests

# Add dev dependencies
uv add --dev pytest

# Sync environment
uv sync

# Run code (no venv activation needed!)
uv run python -m band_name_generator
```

## License

This project is provided as-is for educational and entertainment purposes.

---

**Examples of famous band names this generator emulates:**
- Depeche Mode (compound/foreign words)
- Iron Maiden (metal + noun)
- Limp Bizkit (adjective + noun)
- The Rolling Stones (the + verb + noun plural)
- Red Hot Chili Peppers (color + adjective + noun plural)
- Deep Purple (adjective + color)
- Black Sabbath (color + noun)
