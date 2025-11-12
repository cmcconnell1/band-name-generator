# Band Name Generator - Project Structure

This repository contains Python boilerplate templates and standards for Rust-based uv.

## Modern UV Workflow - Quick Reference

**CRITICAL: NO VENV ACTIVATION NEEDED!** Use `uv run` for everything:

```bash
# Code Quality
uv run ruff format .        # Format code
uv run ruff check .         # Lint code
uv run mypy src/            # Type check

# Testing
uv run pytest               # Run tests
uv run pytest --cov         # With coverage

# Running
uv run python -m band_name_generator        # Run this project
uv run python -m band_name_generator -n 10  # Generate 10 names

# Dependencies
uv add package-name         # Add dependency
uv sync                     # Sync environment
```

## Directory Structure

```
band-name-generator/
├── .claude/                      # Claude Code AI configuration
│   ├── project-rules.md         # AI assistant rules
│   └── settings.local.json      # Local settings
│
├── docs/                         # Documentation
│   ├── BAND-NAME-GENERATOR.md   # Band name generator documentation
│   ├── BOILERPLATE-README.md    # Boilerplate usage guide
│   ├── PROJECT-STRUCTURE.md     # This file - project organization
│   ├── PYTHON-BOILERPLATE-INDEX.md  # Quick reference index
│   └── UV-RUST-STANDARD.md      # Complete uv standard documentation
│
├── scripts/                      # Setup utilities
│   ├── setup-python-uv.sh       # Legacy: uv pip-based setup
│   └── setup-python-uv-modern.sh # Modern: Native uv setup (RECOMMENDED)
│
├── src/                          # Source code
│   └── band_name_generator/     # Main package (note: underscores, not dashes)
│       └── __init__.py
│
├── templates/                    # Boilerplate templates for new projects
│   ├── .gitignore.python.template    # Python .gitignore patterns
│   ├── Makefile.template             # Legacy Makefile (uv pip)
│   ├── Makefile.modern.template      # Modern Makefile (native uv)
│   └── pyproject.toml.template       # Comprehensive Python config
│
├── tests/                        # Test files
│   └── __init__.py
│
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore patterns
├── CLAUDE.md                     # Claude Code project context
├── pyproject.toml                # Project configuration
└── README.md                     # Main project README
```

## Purpose

This repository serves as a **reference and template repository** for Python projects using Rust-based uv.

### Key Components

#### 1. Documentation (`docs/`)
- **UV-RUST-STANDARD.md** - The definitive guide to using Rust-based uv
- **BOILERPLATE-README.md** - How to use the boilerplate files
- **PYTHON-BOILERPLATE-INDEX.md** - Quick reference for choosing files
- **PROJECT-STRUCTURE.md** - This file - project organization guide
- **BAND-NAME-GENERATOR.md** - Band name generator feature documentation

#### 2. Templates (`templates/`)
Boilerplate files to copy to new projects:
- Configuration templates (pyproject.toml, Makefile)
- .gitignore patterns
- Both modern and legacy approaches

#### 3. Scripts (`scripts/`)
Setup scripts for boilerplate templates:
- **setup-python-uv-modern.sh** - For NEW projects (uses native uv commands)
- **setup-python-uv.sh** - For EXISTING projects (uses uv pip interface)

#### 4. Project Files (root)
- **pyproject.toml** - This project's configuration
- **CLAUDE.md** - Instructions for Claude Code AI
- **.claude/project-rules.md** - AI assistant rules

## Usage

### For New Python Projects

1. Copy modern templates:
   ```bash
   cp templates/Makefile.modern.template new-project/Makefile
   cp scripts/setup-python-uv-modern.sh new-project/
   ```

2. Run setup:
   ```bash
   cd new-project
   ./setup-python-uv-modern.sh
   ```

### For Existing Projects

1. Copy legacy templates:
   ```bash
   cp scripts/setup-python-uv.sh existing-project/
   ```

2. Run setup:
   ```bash
   cd existing-project
   ./setup-python-uv.sh
   ```

## Important Notes

### Python Package Naming
- **Project name** (in pyproject.toml): Can use dashes (`band-name-generator`)
- **Package directory**: MUST use underscores (`band_name_generator`)
- Python imports can't have dashes, only underscores

### Modern vs Legacy
- **Modern** = Uses native uv commands (`uv add`, `uv sync`, `uv run`)
- **Legacy** = Uses uv pip interface (`uv pip install`, `uv pip compile`)
- Prefer modern for new projects

### Integration with claude-setup-project
This repository's templates should be used by the `~/bin/claude-setup-project` script to:
1. Detect Python projects
2. Copy appropriate templates
3. Run setup scripts
4. Configure Claude Code rules

## Maintenance

When updating boilerplate files:
1. Update templates in `templates/`
2. Update setup scripts in `scripts/`
3. Update documentation in `docs/`
4. Test with a sample project
5. Update version numbers in documentation

## Standards

**MANDATORY:** All Python projects must use Rust-based uv from Astral.
- NO pip
- NO conda
- NO poetry
- ONLY uv

See `UV-RUST-STANDARD.md` (in this directory) for complete standards.

---

Last updated: 2025-11-11
