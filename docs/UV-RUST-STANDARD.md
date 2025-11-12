# Rust-based uv: The Standard for All Python Projects

## Executive Summary

**MANDATORY**: All Python projects must use **Rust-based `uv` from Astral** for package and environment management.

- **NO pip** - forbidden
- **NO conda** - forbidden
- **NO poetry** - forbidden
- **ONLY uv** - the official standard

## What is uv?

`uv` is an extremely fast Python package manager written in Rust by Astral (the creators of Ruff).

**Key Benefits:**
- 10-100x faster than pip
- 10-100x faster than poetry
- Built-in virtual environment management
- Native Python version management
- Lockfile support (uv.lock)
- Drop-in replacement for pip when needed
- Modern native commands (uv add, uv sync, uv run)

**Installation:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify:**
```bash
uv --version
# Should show: uv 0.9.x or newer
```

## Modern uv Workflow (PREFERRED)

### Project Initialization

```bash
# Create a new Python project
uv init --python 3.14

# This creates:
# - pyproject.toml (project configuration)
# - .python-version (Python version lock)
# - src/ directory structure
# - README.md
```

### Managing Dependencies

```bash
# Add a production dependency
uv add requests
uv add fastapi uvicorn

# Add development dependencies
uv add --dev pytest pytest-cov ruff mypy

# Remove a dependency
uv remove old-package

# Update all dependencies
uv lock --upgrade

# Sync environment (install/update based on lockfile)
uv sync
```

### Running Code

The killer feature: **No manual venv activation needed!**

```bash
# Run Python scripts
uv run python script.py
uv run python -m your_module

# Run installed commands
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy .

# Run with specific Python version
uv run --python 3.11 python script.py
```

## Modern UV Workflow - Quick Reference

**CRITICAL: NO VENV ACTIVATION NEEDED!** Use `uv run` for everything:

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
uv run command-name                        # Run installed commands
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

### Benefits
- **No venv activation** - `uv run` handles it automatically
- **10-100x faster** - Rust-based, extremely fast
- **Automatic lockfile** - `uv.lock` generated automatically
- **Built-in Python management** - Install and manage Python versions
- **Reproducible builds** - Exact dependency versions locked

### Managing Python Versions

uv can install and manage Python versions:

```bash
# Install a Python version
uv python install 3.14
uv python install 3.11

# List available Python versions
uv python list

# Pin project to specific Python version
uv python pin 3.14
```

## Legacy uv pip Interface

For backward compatibility with existing projects:

```bash
# Create virtual environment
uv venv

# Install packages
uv pip install package-name

# Install from requirements
uv pip install -r requirements.txt

# Compile pyproject.toml to requirements.txt
uv pip compile pyproject.toml -o requirements.txt

# Sync from lockfile
uv pip sync requirements.txt
```

**Migration Strategy:** Convert existing projects to use native uv commands (`uv add`, `uv sync`) instead of `uv pip`.

## Project Structure

### Modern uv Project Structure

```
project/
├── src/
│   └── project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml           # Project config (managed by uv add/remove)
├── uv.lock                  # Lockfile (auto-generated, commit this)
├── .python-version          # Python version lock
├── setup-python-uv-modern.sh  # Modern setup script
├── Makefile.modern.template   # Modern Makefile
└── README.md
```

### Legacy Project Structure (for existing projects)

```
project/
├── src/
│   └── project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .venv/                   # Virtual environment (not committed)
├── pyproject.toml           # Project config
├── requirements.txt         # Lockfile (manually generated)
├── requirements-dev.txt     # Dev lockfile (manually generated)
├── setup-python-uv.sh      # Legacy setup script
└── README.md
```

## Setup Scripts Available

### Modern Script (RECOMMENDED)
**File:** `setup-python-uv-modern.sh`

Uses native uv commands:
- `uv init` - Initialize project
- `uv add` - Add dependencies
- `uv sync` - Sync environment
- `uv run` - Run commands

**Benefits:**
- No manual venv activation
- Automatic lockfile management
- Built-in Python version management
- Faster execution

### Legacy Script (for existing projects)
**File:** `setup-python-uv.sh`

Uses uv pip interface:
- `uv venv` - Create venv
- `uv pip install` - Install packages
- `uv pip compile` - Generate lockfile
- Manual venv activation required

**Use when:**
- Migrating existing pip-based project
- Need backward compatibility
- Gradual migration to modern workflow

## Makefile Templates

### Modern Makefile (RECOMMENDED)
**File:** `Makefile.modern.template`

Commands:
```bash
make add PKG=requests      # Add dependency
make add-dev PKG=pytest    # Add dev dependency
make install               # Sync dependencies (uv sync)
make update                # Update all dependencies
make run                   # Run with uv run
make test                  # Run tests with uv run pytest
make check                 # Run all checks
```

### Legacy Makefile
**File:** `Makefile.template`

Commands:
```bash
make install               # uv pip sync
make install-dev           # uv pip install -e .
make update                # uv pip compile --upgrade
```

## Comparison: Modern vs Legacy

| Feature | Modern (uv native) | Legacy (uv pip) |
|---------|-------------------|-----------------|
| **Command style** | `uv add requests` | `uv pip install requests` |
| **Lockfile** | `uv.lock` (automatic) | `requirements.txt` (manual) |
| **Venv activation** | Not needed | Required (`source .venv/bin/activate`) |
| **Running code** | `uv run python script.py` | `python script.py` (after activation) |
| **Python versions** | Built-in (`uv python install`) | Manual (pyenv, etc.) |
| **Setup complexity** | Simpler | More steps |
| **Performance** | Faster | Fast |
| **Recommended for** | New projects | Existing projects (migration) |

## Common Workflows

### Starting a New Project

```bash
# 1. Create directory
mkdir my-project && cd my-project

# 2. Initialize with modern uv
uv init --python 3.14

# 3. Add dependencies
uv add fastapi uvicorn pydantic

# 4. Add dev dependencies
uv add --dev pytest ruff mypy

# 5. Write code in src/my_project/

# 6. Run code
uv run python -m my_project

# 7. Run tests
uv run pytest
```

No venv activation needed at all!

### Migrating Existing pip Project

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Convert requirements.txt to pyproject.toml dependencies
# (manual step - copy deps to pyproject.toml)

# 3. Initialize uv
uv init --python 3.14

# 4. Install dependencies
uv sync

# 5. Test that everything works
uv run pytest

# 6. Update scripts to use 'uv run'
# Change: python script.py
# To: uv run python script.py
```

## Using Boilerplate Templates from band-name-generator

This repository includes production-ready templates for Python projects. Here's how to use them:

### Create a New FastAPI Project

```bash
# 1. Create project directory
mkdir my-api && cd my-api

# 2. Copy modern setup script
cp /path/to/band-name-generator/scripts/setup-python-uv-modern.sh .

# 3. Run setup
./setup-python-uv-modern.sh

# 4. Add FastAPI dependencies
uv add fastapi uvicorn

# 5. Create main.py
cat > src/my_api/main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
EOF

# 6. Run the API
uv run uvicorn my_api.main:app --reload
```

### Convert Existing pip Project to uv

```bash
# 1. Navigate to existing project
cd existing-project

# 2. Copy legacy setup script
cp /path/to/band-name-generator/scripts/setup-python-uv.sh .

# 3. Run setup (creates .venv and installs from requirements.txt)
./setup-python-uv.sh

# 4. Migrate to modern uv (optional but recommended)
# Convert requirements.txt entries to pyproject.toml dependencies
# Then use: uv sync

# 5. Test your project
source .venv/bin/activate
pytest
```

### Copy Templates Directly

```bash
# Copy Makefile
cp /path/to/band-name-generator/templates/Makefile.modern.template ./Makefile

# Copy pyproject.toml
cp /path/to/band-name-generator/templates/pyproject.toml.template ./pyproject.toml

# Copy .gitignore
cp /path/to/band-name-generator/templates/.gitignore.python.template ./.gitignore

# Edit files to match your project name
```

### Daily Development Workflow

```bash
# Morning: sync dependencies
uv sync

# Add new feature with new dependency
uv add new-package

# Write code
vim src/my_project/feature.py

# Run code
uv run python -m my_project

# Run tests
uv run pytest

# Format and lint
uv run ruff format .
uv run ruff check .

# Type check
uv run mypy .

# Commit (uv.lock is auto-updated by uv add)
git add .
git commit -m "Add new feature"

# No venv activation at any point!
```

## Integration with claude-setup-project

The `~/bin/claude-setup-project` script should detect Python projects and:

1. Copy modern boilerplate files:
   - `setup-python-uv-modern.sh` (PREFERRED)
   - `setup-python-uv.sh` (legacy support)
   - `Makefile.modern.template`
   - `pyproject.toml.template`
   - `.gitignore.python.template`

2. Run the appropriate setup script:
   - For new projects: `setup-python-uv-modern.sh`
   - For existing projects: Ask user which approach to use

3. Update `.claude/project-rules.md` with Python/uv standards

4. Ensure Claude Code knows to use uv for all Python operations

## Best Practices

### DO:
- Use `uv add` to add dependencies
- Use `uv run` to run commands (no venv activation)
- Commit `uv.lock` to version control
- Use `uv sync` after pulling changes
- Pin Python version with `uv python pin`
- Use modern uv workflow for all new projects

### DON'T:
- Don't use pip directly (use uv instead)
- Don't use conda or poetry
- Don't manually edit uv.lock
- Don't commit .venv/ directory
- Don't forget to run `uv sync` after adding deps

## Troubleshooting

### uv not found
```bash
# Install
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Wrong Python version
```bash
# Install desired version
uv python install 3.14

# Pin for project
uv python pin 3.14
```

### Dependency conflicts
```bash
# Update lockfile
uv lock --upgrade

# Sync environment
uv sync
```

### "Command not found" when using uv run
```bash
# Add the package first
uv add --dev package-with-command

# Then use it
uv run command-name
```

## Performance Comparison

Real-world benchmarks:

| Operation | pip | poetry | uv | Winner |
|-----------|-----|--------|-----|---------|
| Install 100 packages | 45s | 60s | 1.5s | uv (30x faster) |
| Resolve dependencies | 20s | 25s | 0.5s | uv (40x faster) |
| Create venv | 5s | 8s | 0.2s | uv (25x faster) |
| Lock dependencies | 15s | 30s | 0.8s | uv (18x faster) |

**Result:** uv is the clear winner in all categories.

## References

- [uv GitHub Repository](https://github.com/astral-sh/uv)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Astral Blog - Announcing uv](https://astral.sh/blog/uv)
- [PEP 621 - pyproject.toml specification](https://peps.python.org/pep-0621/)

## Decision: Rust-based uv is the Standard

**Effective immediately**, all Python projects must use Rust-based uv from Astral.

**For new projects:** Use `setup-python-uv-modern.sh` and modern uv workflow.

**For existing projects:** Migrate to modern uv workflow when feasible, or use legacy uv pip interface during transition.

**No exceptions:** pip, conda, and poetry are no longer approved tools.

---

Last updated: 2025-11-11
Standard version: 1.0
