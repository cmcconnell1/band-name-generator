#!/bin/bash

# Modern Python Project Setup Script using Rust-based uv
# Uses native uv commands (uv init, uv add, uv sync) - the preferred workflow
#
# CRITICAL: This script sets up the MODERN uv workflow
# - NO VENV ACTIVATION NEEDED!
# - Use 'uv run' for all commands
# - Automatic lockfile management (uv.lock)
# - Built-in Python version management
#
# After setup, use:
#   uv add package-name          # Add dependencies
#   uv run python script.py      # Run code (no activation!)
#   uv run pytest                # Run tests
#   uv sync                      # Sync environment

set -e  # Exit on error

# Configuration
PYTHON_VERSION="${PYTHON_VERSION:-3.14}"
PROJECT_NAME="$(basename "$(pwd)")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if uv is installed (Rust-based version from Astral)
check_uv() {
    if ! command_exists uv; then
        print_error "uv is not installed"
        print_status "Install Rust-based uv with: curl -LsSf https://astral.sh/uv/install.sh | sh"
        print_status "Or visit: https://github.com/astral-sh/uv"
        exit 1
    fi

    local uv_version
    uv_version=$(uv --version 2>&1 | head -n 1)
    print_success "Rust-based uv is installed ($uv_version)"
}

# Initialize project with modern uv
init_project() {
    print_status "Initializing Python project with uv..."

    if [ -f "pyproject.toml" ]; then
        print_warning "pyproject.toml already exists"
        read -p "Do you want to reinitialize? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Skipping initialization, using existing pyproject.toml"
            return
        fi
    fi

    # Use uv init to create a modern Python project
    if uv init --python "$PYTHON_VERSION" --name "$PROJECT_NAME"; then
        print_success "Project initialized with Python $PYTHON_VERSION"
    else
        print_error "Failed to initialize project"
        exit 1
    fi

    # Update pyproject.toml with better defaults
    enhance_pyproject
}

# Enhance pyproject.toml with comprehensive configuration
enhance_pyproject() {
    if [ ! -f "pyproject.toml" ]; then
        return
    fi

    print_status "Enhancing pyproject.toml with tool configurations..."

    # Check if tool configurations already exist
    if grep -q "\[tool.ruff\]" pyproject.toml; then
        print_status "Tool configurations already present"
        return
    fi

    # Append tool configurations
    cat >> pyproject.toml << 'EOF'

# Ruff configuration (formatter and linter)
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "C4", "SIM", "RUF"]
ignore = ["E501"]

[tool.ruff.lint.isort]
known-first-party = ["${PROJECT_NAME}"]

# MyPy configuration (type checker)
[tool.mypy]
python_version = "3.14"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

# Pytest configuration
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = ["--cov", "--cov-report=html", "--cov-report=term-missing"]
EOF

    print_success "Enhanced pyproject.toml with tool configurations"
}

# Add development dependencies using modern uv
add_dev_dependencies() {
    print_status "Adding development dependencies..."

    local dev_deps=(
        "pytest"
        "pytest-cov"
        "ruff"
        "mypy"
    )

    if uv add --dev "${dev_deps[@]}"; then
        print_success "Added development dependencies"
    else
        print_warning "Some dependencies may have failed to install"
    fi
}

# Create project structure
create_project_structure() {
    print_status "Setting up project structure..."

    # Create tests directory if it doesn't exist
    if [ ! -d "tests" ]; then
        mkdir -p tests
        touch tests/__init__.py
        cat > tests/test_example.py << 'EOF'
"""Example test file."""


def test_example() -> None:
    """Example test that always passes."""
    assert True
EOF
        print_success "Created tests/ directory with example test"
    fi

    # Create .env.example if not exists
    if [ ! -f ".env.example" ]; then
        cat > .env.example << 'EOF'
# Environment Variables Template
# Copy this file to .env and fill in your actual values
# NEVER commit .env to version control

# Python environment
PYTHONUNBUFFERED=1

# Application settings
APP_ENV=development
DEBUG=true

# API keys and secrets
# API_KEY=your-api-key-here
# SECRET_KEY=your-secret-key-here
EOF
        print_success "Created .env.example template"
    fi

    # Create .gitignore if not exists
    if [ ! -f ".gitignore" ]; then
        cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
pip-log.txt
pip-delete-this-directory.txt

# Virtual Environments
.venv/
venv/
ENV/
env/
.virtualenv/
virtualenv/
.pyenv/
pyenv/

# UV (Rust-based Python package manager)
.uv/
.uv_cache/

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff
instance/
.webassets-cache

# Scrapy stuff
.scrapy

# Sphinx documentation
docs/_build/
docs/_static/
docs/_templates/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml
pdm.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.env.local
.env.*.local
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
!.env.example

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# Ruff
.ruff_cache/

# LSP
pyrightconfig.json

# IDE and Editor files
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# OS Files
Thumbs.db
.DS_Store

# Logs and temporary files
*.log
*.bak
*.tmp
temp/
tmp/

# Secrets and credentials
secrets/
credentials/
*.pem
*.key
*.crt
api-keys.txt
config.local.json
settings.local.py
EOF
        print_success "Created .gitignore with Python patterns"
    fi

    # Create README.md if not exists
    if [ ! -f "README.md" ]; then
        cat > README.md << EOF
# $PROJECT_NAME

A modern Python project built with Rust-based uv.

## Setup

1. Install uv (Rust-based from Astral):
   \`\`\`bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   \`\`\`

2. Run the setup script:
   \`\`\`bash
   ./setup-python-uv-modern.sh
   \`\`\`

3. Sync dependencies:
   \`\`\`bash
   uv sync
   \`\`\`

## Development

### Adding Dependencies

\`\`\`bash
# Add a production dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Remove a dependency
uv remove package-name
\`\`\`

### Running Code

\`\`\`bash
# Run Python script
uv run python your_script.py

# Run tests
uv run pytest

# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type check
uv run mypy .
\`\`\`

### Updating Dependencies

\`\`\`bash
# Update lockfile
uv lock --upgrade

# Sync environment
uv sync
\`\`\`

## Project Structure

\`\`\`
$PROJECT_NAME/
├── src/
│   └── ${PROJECT_NAME}/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_example.py
├── pyproject.toml       # Project configuration
├── uv.lock             # Dependency lockfile (auto-generated)
└── README.md           # This file
\`\`\`

## Features

- Modern Python project structure
- Rust-based uv for fast dependency management
- Type hints with mypy
- Code formatting and linting with ruff
- Testing with pytest
- No pip, no conda, no poetry - just uv

## Documentation

- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
EOF
        print_success "Created README.md"
    fi
}

# Setup git hooks (optional)
setup_git_hooks() {
    if [ ! -d ".git" ]; then
        print_status "Not a git repository, skipping git hooks"
        return
    fi

    print_status "Setting up pre-commit hooks..."

    # Add pre-commit as dev dependency
    uv add --dev pre-commit

    if [ ! -f ".pre-commit-config.yaml" ]; then
        cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.14
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: detect-private-key
EOF
        print_success "Created .pre-commit-config.yaml"

        # Install pre-commit hooks
        if uv run pre-commit install; then
            print_success "Installed pre-commit hooks"
        fi
    fi
}

# Sync environment
sync_environment() {
    print_status "Syncing environment with dependencies..."

    if uv sync; then
        print_success "Environment synced successfully"
    else
        print_error "Failed to sync environment"
        exit 1
    fi
}

# Main setup flow
main() {
    echo ""
    print_status "Modern Python Project Setup with Rust-based uv"
    print_status "Project: $PROJECT_NAME"
    print_status "Python: $PYTHON_VERSION"
    echo ""

    check_uv
    init_project
    add_dev_dependencies
    create_project_structure
    sync_environment
    setup_git_hooks

    echo ""
    print_success "Setup complete!"
    echo ""
    print_status "Next steps:"
    echo "  1. Add dependencies: uv add package-name"
    echo "  2. Run code: uv run python src/$PROJECT_NAME/main.py"
    echo "  3. Run tests: uv run pytest"
    echo "  4. Format code: uv run ruff format ."
    echo ""
    print_status "All commands use 'uv run' - no virtual environment activation needed!"
    echo ""
    print_status "Modern uv workflow:"
    echo "  - Add deps: uv add package-name"
    echo "  - Dev deps: uv add --dev package-name"
    echo "  - Run code: uv run python script.py"
    echo "  - Sync env: uv sync"
    echo "  - Update: uv lock --upgrade"
    echo ""
}

# Run main function
main
