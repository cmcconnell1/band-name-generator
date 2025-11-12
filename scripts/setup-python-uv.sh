#!/bin/bash

# Legacy Python Project Setup Script using uv pip interface
# Sets up a Python development environment with uv (fast Rust-based package manager)
#
# WARNING: This uses the LEGACY uv pip workflow
# For new projects, use setup-python-uv-modern.sh instead!
#
# This script:
# - Creates a .venv directory (requires manual activation)
# - Uses uv pip commands (uv pip install, uv pip compile)
# - Generates requirements.txt manually
#
# Modern workflow (recommended for new projects):
# - No .venv activation needed
# - Use 'uv run' for everything
# - Automatic lockfile (uv.lock)
# - See: setup-python-uv-modern.sh

set -e  # Exit on error

# Configuration
PYTHON_VERSION="${PYTHON_VERSION:-3.14}"
VENV_DIR=".venv"
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

# Check if uv is installed
check_uv() {
    if ! command_exists uv; then
        print_error "uv is not installed"
        print_status "Install uv with: curl -LsSf https://astral.sh/uv/install.sh | sh"
        print_status "Or visit: https://github.com/astral-sh/uv"
        exit 1
    fi

    print_success "uv is installed ($(uv --version))"
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment with Python $PYTHON_VERSION..."

    if [ -d "$VENV_DIR" ]; then
        print_warning "Virtual environment already exists at $VENV_DIR"
        read -p "Do you want to recreate it? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VENV_DIR"
            print_status "Removed existing virtual environment"
        else
            print_status "Using existing virtual environment"
            return
        fi
    fi

    if uv venv --python "$PYTHON_VERSION" "$VENV_DIR"; then
        print_success "Virtual environment created at $VENV_DIR"
    else
        print_error "Failed to create virtual environment"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."

    # Check for pyproject.toml first (preferred)
    if [ -f "pyproject.toml" ]; then
        print_status "Found pyproject.toml - installing project dependencies"

        # Install the project in editable mode
        if uv pip install -e .; then
            print_success "Installed project dependencies from pyproject.toml"
        else
            print_error "Failed to install from pyproject.toml"
            exit 1
        fi

        # Install dev dependencies if specified
        if [ -f "requirements-dev.txt" ]; then
            print_status "Installing development dependencies..."
            if uv pip install -r requirements-dev.txt; then
                print_success "Installed development dependencies"
            else
                print_warning "Failed to install some development dependencies"
            fi
        fi

    # Fall back to requirements.txt
    elif [ -f "requirements.txt" ]; then
        print_status "Found requirements.txt - installing dependencies"

        if uv pip install -r requirements.txt; then
            print_success "Installed dependencies from requirements.txt"
        else
            print_error "Failed to install from requirements.txt"
            exit 1
        fi

        # Install dev dependencies if specified
        if [ -f "requirements-dev.txt" ]; then
            print_status "Installing development dependencies..."
            if uv pip install -r requirements-dev.txt; then
                print_success "Installed development dependencies"
            else
                print_warning "Failed to install some development dependencies"
            fi
        fi

    else
        print_warning "No pyproject.toml or requirements.txt found"
        print_status "Creating basic pyproject.toml template..."
        create_pyproject_template
    fi
}

# Create pyproject.toml template
create_pyproject_template() {
    if [ -f "pyproject.toml" ]; then
        print_warning "pyproject.toml already exists, skipping template creation"
        return
    fi

    cat > pyproject.toml << EOF
[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "A Python project"
readme = "README.md"
requires-python = ">=$PYTHON_VERSION"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    "mypy>=1.8.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]

[tool.mypy]
python_version = "$PYTHON_VERSION"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov --cov-report=html --cov-report=term-missing"
EOF

    print_success "Created pyproject.toml template"
}

# Create basic project structure
create_project_structure() {
    print_status "Setting up project structure..."

    # Create src directory if it doesn't exist
    if [ ! -d "src" ] && [ ! -d "$PROJECT_NAME" ]; then
        mkdir -p "src/$PROJECT_NAME"
        touch "src/$PROJECT_NAME/__init__.py"
        print_success "Created src/$PROJECT_NAME/ directory"
    fi

    # Create tests directory
    if [ ! -d "tests" ]; then
        mkdir -p tests
        touch tests/__init__.py
        print_success "Created tests/ directory"
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
# APP_ENV=development
# DEBUG=true

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

    # Create basic README if not exists
    if [ ! -f "README.md" ]; then
        cat > README.md << EOF
# $PROJECT_NAME

A Python project built with uv.

## Setup

1. Install uv:
   \`\`\`bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   \`\`\`

2. Run the setup script:
   \`\`\`bash
   ./setup-python-uv.sh
   \`\`\`

3. Activate the virtual environment:
   \`\`\`bash
   source .venv/bin/activate
   \`\`\`

## Development

- Run tests: \`pytest\`
- Format code: \`ruff format .\`
- Lint code: \`ruff check .\`
- Type check: \`mypy .\`

## Dependencies

Dependencies are managed using uv. To add a new dependency:

\`\`\`bash
# Add to pyproject.toml dependencies array, then:
uv pip compile pyproject.toml -o requirements.txt
uv pip sync requirements.txt
\`\`\`
EOF
        print_success "Created README.md"
    fi
}

# Generate requirements.txt from pyproject.toml
generate_requirements() {
    if [ -f "pyproject.toml" ] && ! [ -f "requirements.txt" ]; then
        print_status "Generating requirements.txt from pyproject.toml..."

        if uv pip compile pyproject.toml -o requirements.txt; then
            print_success "Generated requirements.txt"
        else
            print_warning "Could not generate requirements.txt"
        fi

        if uv pip compile --extra dev pyproject.toml -o requirements-dev.txt; then
            print_success "Generated requirements-dev.txt"
        else
            print_warning "Could not generate requirements-dev.txt"
        fi
    fi
}

# Setup git hooks (optional)
setup_git_hooks() {
    if [ -d ".git" ] && [ -f "pyproject.toml" ]; then
        print_status "Setting up pre-commit hooks..."

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
        fi
    fi
}

# Main setup flow
main() {
    echo ""
    print_status "Python Project Setup with uv"
    print_status "Project: $PROJECT_NAME"
    print_status "Python: $PYTHON_VERSION"
    echo ""

    check_uv
    create_venv
    create_pyproject_template
    create_project_structure
    install_dependencies
    generate_requirements
    setup_git_hooks

    echo ""
    print_success "Setup complete!"
    echo ""
    print_status "Next steps:"
    echo "  1. Activate virtual environment: source $VENV_DIR/bin/activate"
    echo "  2. Start coding in src/$PROJECT_NAME/"
    echo "  3. Add tests in tests/"
    echo "  4. Run tests with: pytest"
    echo ""
    print_status "Useful commands:"
    echo "  - Install package: uv pip install <package>"
    echo "  - Update requirements: uv pip compile pyproject.toml -o requirements.txt"
    echo "  - Format code: ruff format ."
    echo "  - Lint code: ruff check ."
    echo "  - Type check: mypy ."
    echo ""
}

# Run main function
main
