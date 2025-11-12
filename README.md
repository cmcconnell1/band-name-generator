# Python Project Boilerplate Templates

A comprehensive collection of boilerplate templates and setup scripts for Python projects using **Rust-based uv** from Astral.

## Quick Start

### For New Projects (Recommended)

```bash
# 1. Copy the modern setup script
cp scripts/setup-python-uv-modern.sh /path/to/new-project/

# 2. Copy templates
cp templates/Makefile.modern.template /path/to/new-project/Makefile
cp templates/.gitignore.python.template /path/to/new-project/.gitignore

# 3. Run setup
cd /path/to/new-project
./setup-python-uv-modern.sh
```

### For Existing Projects

```bash
# Use the legacy setup script for backward compatibility
cp scripts/setup-python-uv.sh /path/to/existing-project/
cd /path/to/existing-project
./setup-python-uv.sh
```

## What's Included

### Band Name Generator (Example Implementation)

A fully-featured band name generator demonstrating modern Python development:

```bash
# List available patterns
uv run python -m band_name_generator -l

# Generate names with specific patterns
uv run python -m band_name_generator -p metal_noun -n 5                  # Iron Maiden style
uv run python -m band_name_generator -p color_noun -n 5                  # Black Sabbath style
uv run python -m band_name_generator -p the_adjective_noun -n 5          # The Rolling Stones style
uv run python -m band_name_generator -p color_adjective_noun_plural -n 5 # Red Hot Chili Peppers style

# Generate random names
uv run python -m band_name_generator -n 10
```

**Features:**
- 10 different name patterns (2-word, 3-word, and 4-word combinations)
- Includes specific pattern for "Red Hot Chili Peppers" style names (color + adjective + noun + plural)
- 30+ tests with 97% coverage
- Full type hints with mypy
- CLI with argparse
- See [BAND-NAME-GENERATOR.md](docs/BAND-NAME-GENERATOR.md) for complete documentation

### Documentation (`docs/`)
- **UV-RUST-STANDARD.md** - Complete standard for using Rust-based uv
- **BOILERPLATE-README.md** - Detailed usage guide for all templates
- **PYTHON-BOILERPLATE-INDEX.md** - Quick reference and decision tree
- **BAND-NAME-GENERATOR.md** - Band name generator documentation with CLI examples
- **PROJECT-STRUCTURE.md** - Repository organization guide

### Setup Scripts (`scripts/`)
- **setup-python-uv-modern.sh** - Modern setup using native uv commands (NEW projects)
- **setup-python-uv.sh** - Legacy setup using uv pip interface (EXISTING projects)
- **band-name-gen.py** - Example Python script

### Templates (`templates/`)
- **Makefile.modern.template** - Makefile with native uv commands
- **Makefile.template** - Makefile with uv pip commands
- **pyproject.toml.template** - Comprehensive Python project configuration
- **.gitignore.python.template** - Python-specific gitignore patterns

## The Standard: Rust-based uv

**MANDATORY:** All Python projects must use Rust-based uv from Astral.

### Why uv?
- 10-100x faster than pip
- Written in Rust for maximum performance
- Built-in virtual environment management
- Native Python version management
- Modern lockfile support

### Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Modern Workflow

```bash
# Initialize project
uv init --python 3.14

# Add dependencies
uv add requests fastapi

# Add dev dependencies
uv add --dev pytest ruff mypy

# Sync environment
uv sync

# Run code (no venv activation needed!)
uv run python script.py
uv run pytest
```

## Modern UV Workflow - Quick Reference

**NO VENV ACTIVATION NEEDED!** Use `uv run` for everything:

### Code Quality

```bash
uv run ruff format .        # Format code
uv run ruff check .         # Lint code
uv run ruff check --fix .   # Fix issues automatically
uv run mypy src/            # Type check
```

### Testing

```bash
uv run pytest               # Run tests
uv run pytest -v            # Verbose output
uv run pytest --cov         # With coverage report
```

### Running Code

```bash
uv run python script.py                    # Run Python scripts
uv run python -m module_name               # Run modules
uv run python -m band_name_generator       # Run this project
```

### Dependency Management

```bash
uv add package-name         # Add production dependency
uv add --dev package-name   # Add development dependency
uv remove package-name      # Remove dependency
uv sync                     # Sync environment with lockfile
uv lock --upgrade           # Update lockfile to latest versions
```

### Python Version Management

```bash
uv python install 3.14      # Install Python 3.14
uv python list              # List available Python versions
uv python pin 3.14          # Pin project to Python 3.14
```

### Benefits of Modern uv Workflow

- **No venv activation** - `uv run` handles it automatically
- **10-100x faster** - Rust-based, extremely fast
- **Automatic lockfile** - `uv.lock` generated automatically
- **Built-in Python management** - Install and manage Python versions
- **Reproducible builds** - Exact dependency versions locked

## Project Structure

```
band-name-generator/
├── docs/              # Documentation
├── scripts/           # Setup scripts and utilities
├── templates/         # Boilerplate templates
├── src/               # Source code (example)
├── tests/             # Tests (example)
└── .claude/           # Claude Code AI configuration
```

See [PROJECT-STRUCTURE.md](docs/PROJECT-STRUCTURE.md) for detailed structure.

## Documentation

| Document | Description |
|----------|-------------|
| [UV-RUST-STANDARD.md](docs/UV-RUST-STANDARD.md) | Complete uv standard and guide |
| [BOILERPLATE-README.md](docs/BOILERPLATE-README.md) | How to use boilerplate files |
| [PYTHON-BOILERPLATE-INDEX.md](docs/PYTHON-BOILERPLATE-INDEX.md) | Quick reference index |
| [PROJECT-STRUCTURE.md](docs/PROJECT-STRUCTURE.md) | This repository's organization |
| [BAND-NAME-GENERATOR.md](docs/BAND-NAME-GENERATOR.md) | Band name generator documentation |

## Modern vs Legacy

### Modern Approach (Recommended)

**Use for:** New projects

**Features:**
- Native uv commands (`uv add`, `uv sync`, `uv run`)
- No venv activation needed
- Automatic lockfile (uv.lock)
- Built-in Python version management

**Files:**
- `scripts/setup-python-uv-modern.sh`
- `templates/Makefile.modern.template`

### Legacy Approach

**Use for:** Existing projects, gradual migration

**Features:**
- uv pip interface (`uv pip install`, `uv pip compile`)
- Requires manual venv activation
- requirements.txt based
- Familiar to pip users

**Files:**
- `scripts/setup-python-uv.sh`
- `templates/Makefile.template`

## Integration with ~/bin/claude-setup-project

These templates are designed to integrate with the `claude-setup-project` script:

```bash
# The script should detect Python projects and:
# 1. Copy appropriate templates
# 2. Run setup scripts
# 3. Configure Claude Code rules
```

## Examples

### Using the Band Name Generator

```bash
# Clone this repository
cd band-name-generator

# Install dependencies (if not already done)
uv sync

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

# See all 10 available patterns
$ uv run python -m band_name_generator -l
```

For complete documentation with all pattern examples, see [BAND-NAME-GENERATOR.md](docs/BAND-NAME-GENERATOR.md).

### Create a New FastAPI Project

```bash
mkdir my-api && cd my-api
cp /path/to/band-name-generator/scripts/setup-python-uv-modern.sh .
./setup-python-uv-modern.sh

uv add fastapi uvicorn
uv run uvicorn main:app --reload
```

### Convert Existing pip Project

```bash
cd existing-project
cp /path/to/band-name-generator/scripts/setup-python-uv.sh .
./setup-python-uv.sh

# Migrate dependencies to pyproject.toml
# Then use: uv pip sync requirements.txt
```

## Standards and Rules

### Package Naming
- **Project name**: Can use dashes (`my-project`)
- **Package directory**: MUST use underscores (`my_project`)
- Python imports require underscores

### Required Tools
- **uv** - MANDATORY (Rust-based from Astral)
- **ruff** - For formatting and linting
- **mypy** - For type checking
- **pytest** - For testing

### Forbidden Tools
- **pip** - Use uv instead
- **conda** - Use uv instead
- **poetry** - Use uv instead

## Contributing

When updating templates:
1. Test with a sample project
2. Update documentation
3. Update version numbers
4. Commit changes

## Resources

- [uv GitHub](https://github.com/astral-sh/uv)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)

## License

These templates are provided as-is for use in any Python project.

---

**Standard Version:** 1.0
**Last Updated:** 2025-11-11
**Maintained by:** Personal development standards
