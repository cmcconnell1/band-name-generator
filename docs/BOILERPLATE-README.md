# Python Project Boilerplate Files

This directory contains boilerplate templates and setup scripts for Python projects using **Rust-based `uv` from Astral**.

## Overview

These files enforce standardized Python development practices across all projects:
- **Rust-based uv** - MANDATORY (10-100x faster than pip)
- **NO pip, NO conda, NO poetry** - uv is the only approved tool
- Modern project structure with `pyproject.toml`
- Code quality tools (ruff, mypy, pytest)
- Security best practices
- No emojis policy

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

## Files Included

### Setup Scripts

#### `setup-python-uv.sh`
Automated setup script that initializes a complete Python development environment.

**What it does:**
- Checks if `uv` is installed
- Creates Python virtual environment with specified version
- Installs dependencies from pyproject.toml or requirements.txt
- Generates project structure (src/, tests/, .env.example)
- Creates pyproject.toml if missing
- Generates requirements.txt lockfile
- Sets up pre-commit hooks configuration
- Creates basic README.md

**Usage:**
```bash
./setup-python-uv.sh
```

**Environment variables:**
- `PYTHON_VERSION` - Python version to use (default: 3.14)

**Example:**
```bash
PYTHON_VERSION=3.11 ./setup-python-uv.sh
```

### Configuration Templates

#### `pyproject.toml.template`
Comprehensive Python project configuration following PEP 621 standards.

**Includes:**
- Project metadata (name, version, description, authors)
- Dependencies configuration
- Optional dependency groups (dev, web, data)
- Build system configuration (hatchling)
- Ruff configuration (formatter and linter)
- MyPy configuration (type checker)
- Pytest configuration (testing framework)
- Coverage configuration

**Usage:**
```bash
cp pyproject.toml.template pyproject.toml
# Edit the file to customize for your project
```

**Sections to customize:**
- `[project]` - Update name, version, description, authors
- `dependencies` - Add your runtime dependencies
- `[project.optional-dependencies]` - Add optional dependency groups
- `[project.scripts]` - Define CLI entry points
- `[tool.hatch.build.targets.wheel]` - Update package path

#### `Makefile.template`
Common development commands for Python projects.

**Available commands:**
- `make install` - Install production dependencies
- `make install-dev` - Install development dependencies
- `make update` - Update all dependencies
- `make format` - Format code with ruff
- `make lint` - Lint code with ruff
- `make type-check` - Run type checking with mypy
- `make test` - Run tests with pytest
- `make coverage` - Run tests with coverage report
- `make clean` - Remove build artifacts
- `make build` - Build distribution packages
- `make check` - Run all checks before commit
- `make setup` - Complete development environment setup

**Usage:**
```bash
cp Makefile.template Makefile
# Customize the 'run' target for your application
make help
```

#### `.gitignore.python.template`
Comprehensive .gitignore for Python projects.

**Includes patterns for:**
- Python virtual environments (.venv, venv, etc.)
- Compiled Python files (\_\_pycache\_\_, *.pyc)
- Distribution files (build/, dist/, *.egg-info)
- Test and coverage files (.pytest_cache, .coverage)
- IDE files (.vscode, .idea)
- Environment files (.env)
- uv cache files (.ruff_cache, .uv)
- Secrets and credentials

**Usage:**
```bash
# For new projects
cp .gitignore.python.template .gitignore

# For existing projects (merge manually)
cat .gitignore.python.template >> .gitignore
```

### Documentation Files

#### `.claude/project-rules.md`
Updated with Python/uv specific guidelines including:
- Mandatory uv usage for all Python projects
- Virtual environment management commands
- Package management best practices
- Project structure standards
- Code quality tool configuration
- Security standards for Python projects

#### `CLAUDE.md`
Updated with comprehensive Python/uv setup instructions including:
- Technology stack specification
- Development environment setup steps
- Common uv commands
- Makefile usage
- Project structure diagram
- Boilerplate file descriptions

## Quick Start Guide

### For New Python Projects

1. Create project directory:
   ```bash
   mkdir my-project && cd my-project
   ```

2. Copy boilerplate files:
   ```bash
   cp /path/to/boilerplate/setup-python-uv.sh .
   cp /path/to/boilerplate/pyproject.toml.template pyproject.toml
   cp /path/to/boilerplate/Makefile.template Makefile
   cp /path/to/boilerplate/.gitignore.python.template .gitignore
   ```

3. Run setup script:
   ```bash
   chmod +x setup-python-uv.sh
   ./setup-python-uv.sh
   ```

4. Activate virtual environment:
   ```bash
   source .venv/bin/activate
   ```

5. Start coding:
   ```bash
   # Your code goes in src/your_package/
   # Tests go in tests/
   ```

### For Existing Python Projects

1. Install uv:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Copy setup script:
   ```bash
   cp /path/to/boilerplate/setup-python-uv.sh .
   chmod +x setup-python-uv.sh
   ```

3. Merge configurations:
   ```bash
   # Review and merge pyproject.toml sections
   # Review and merge .gitignore patterns
   # Copy Makefile if desired
   ```

4. Run setup:
   ```bash
   ./setup-python-uv.sh
   ```

## Project Structure

After running the setup script, your project will have this structure:

```
my-project/
├── .venv/                          # Virtual environment (not committed)
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .claude/
│   └── project-rules.md           # Claude Code AI rules
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Locked dependencies (committed)
├── requirements-dev.txt           # Locked dev dependencies (committed)
├── setup-python-uv.sh            # Setup script
├── Makefile                       # Development commands
├── .gitignore                     # Git ignore patterns
├── .env.example                   # Environment variables template
├── .pre-commit-config.yaml       # Pre-commit hooks config
├── CLAUDE.md                      # Claude Code project context
└── README.md                      # Project documentation
```

## Best Practices

### Dependency Management

1. **Add new dependencies:**
   ```bash
   # Edit pyproject.toml dependencies array
   uv pip compile pyproject.toml -o requirements.txt
   uv pip sync requirements.txt
   ```

2. **Update dependencies:**
   ```bash
   uv pip compile --upgrade pyproject.toml -o requirements.txt
   uv pip sync requirements.txt
   ```

3. **Install in new environment:**
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip sync requirements.txt
   ```

### Code Quality Workflow

1. **Before committing:**
   ```bash
   make format      # Format code
   make lint        # Check linting
   make type-check  # Check types
   make test        # Run tests
   ```

2. **Or use the combined check:**
   ```bash
   make check
   ```

3. **Or set up pre-commit hooks:**
   ```bash
   make setup
   # Now hooks run automatically on git commit
   ```

### Development Workflow

1. **Create feature branch:**
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Write code and tests:**
   ```bash
   # Edit files in src/
   # Add tests in tests/
   ```

3. **Run checks:**
   ```bash
   make check
   ```

4. **Commit changes:**
   ```bash
   git add .
   git commit -m "Add my feature"
   ```

5. **Push to remote:**
   ```bash
   git push origin feature/my-feature
   ```

## Tool Configuration Details

### Ruff (Formatter and Linter)

Ruff is configured to replace multiple tools:
- Replaces Black (formatter)
- Replaces flake8 (linter)
- Replaces isort (import sorting)
- Replaces pylint (code quality)

Configuration in `pyproject.toml`:
- Line length: 100 characters
- Target: Python 3.14
- Enabled rules: E, W, F, I, N, UP, B, C4, and more
- Google-style docstrings

### MyPy (Type Checker)

Strict type checking configuration:
- Requires type hints on all functions
- Disallows untyped function calls
- Warns on unused ignores
- Pretty error output

### Pytest (Testing Framework)

Configuration includes:
- Automatic test discovery
- Coverage reporting (HTML and terminal)
- Branch coverage enabled
- Custom markers (slow, integration, unit)

## Security Considerations

1. **Never commit secrets:**
   - Use .env files (excluded by .gitignore)
   - Use environment variables
   - Use secret management tools (AWS Secrets Manager, etc.)

2. **Pin dependencies:**
   - requirements.txt locks exact versions
   - Prevents unexpected updates
   - Ensures reproducible builds

3. **Regular audits:**
   ```bash
   uv pip list --outdated
   # Review and update dependencies regularly
   ```

4. **Pre-commit hooks:**
   - Automatically check for secrets
   - Check for large files
   - Detect merge conflicts

## Integration with ~/bin/claude-setup-project

These boilerplate files are designed to work with the `claude-setup-project` script.

When `claude-setup-project` detects a Python project, it should:
1. Copy these template files to the project
2. Run `setup-python-uv.sh`
3. Set up Claude Code configuration files
4. Initialize git repository if needed

## Troubleshooting

### uv not found
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH
export PATH="$HOME/.cargo/bin:$PATH"
```

### Python version not found
```bash
# uv can install Python versions
uv python install 3.14

# Or specify a different version
PYTHON_VERSION=3.11 ./setup-python-uv.sh
```

### Permission denied on setup script
```bash
chmod +x setup-python-uv.sh
```

### Dependencies not installing
```bash
# Clean and reinstall
rm -rf .venv
./setup-python-uv.sh
```

## References

- [uv Documentation](https://github.com/astral-sh/uv)
- [PEP 621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

## Maintenance

These boilerplate files should be reviewed and updated:
- When new Python best practices emerge
- When tool configurations change
- When security recommendations are updated
- At least quarterly for dependency updates

Last updated: 2025-11-11
