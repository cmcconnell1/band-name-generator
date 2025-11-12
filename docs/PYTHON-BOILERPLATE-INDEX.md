# Python Boilerplate Files - Complete Index

**Standard:** All Python projects MUST use Rust-based uv from Astral (NOT pip, NOT conda, NOT poetry)

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

### Dependency Management
```bash
uv add package-name         # Add production dependency
uv add --dev package-name   # Add development dependency
uv sync                     # Sync environment with lockfile
uv lock --upgrade           # Update dependencies
```

## Quick Reference

### For NEW Projects (RECOMMENDED)
1. Copy `setup-python-uv-modern.sh` and run it
2. Copy `Makefile.modern.template` to `Makefile`
3. Use modern uv commands: `uv add`, `uv sync`, `uv run`

### For EXISTING Projects
1. Copy `setup-python-uv.sh` and run it (uses uv pip interface)
2. Copy `Makefile.template` to `Makefile`
3. Gradually migrate to modern uv workflow

## File Inventory

### Setup Scripts

| File | Purpose | When to Use |
|------|---------|-------------|
| `setup-python-uv-modern.sh` | Modern setup using native uv commands | NEW projects (preferred) |
| `setup-python-uv.sh` | Legacy setup using uv pip interface | EXISTING projects |

### Makefile Templates

| File | Purpose | When to Use |
|------|---------|-------------|
| `Makefile.modern.template` | Modern commands (uv add, uv sync, uv run) | NEW projects (preferred) |
| `Makefile.template` | Legacy commands (uv pip) | EXISTING projects |

### Configuration Templates

| File | Purpose | Notes |
|------|---------|-------|
| `pyproject.toml.template` | Project configuration | Works with both modern and legacy |
| `.gitignore.python.template` | Python gitignore patterns | Merge with existing .gitignore |

### Documentation

| File | Purpose | Audience |
|------|---------|----------|
| `UV-RUST-STANDARD.md` | Comprehensive uv standard guide | Developers |
| `BOILERPLATE-README.md` | Boilerplate file documentation | Project setup |
| `PROJECT-STRUCTURE.md` | Project organization guide | Developers |
| `BAND-NAME-GENERATOR.md` | Band name generator docs | Users |
| `PYTHON-BOILERPLATE-INDEX.md` | This file | Quick reference |
| `../CLAUDE.md` | Claude Code project context | AI assistant |
| `../.claude/project-rules.md` | AI assistant rules | AI assistant |

## Modern vs Legacy Approach

### Modern Approach (PREFERRED for new projects)

**Setup:**
```bash
./setup-python-uv-modern.sh
```

**Daily workflow:**
```bash
uv add requests          # Add dependency
uv add --dev pytest      # Add dev dependency
uv sync                  # Sync environment
uv run python script.py  # Run code
uv run pytest            # Run tests
```

**Benefits:**
- No venv activation needed
- Automatic lockfile (uv.lock)
- Built-in Python version management
- Simpler workflow

**Project structure:**
```
project/
├── src/project/
├── tests/
├── pyproject.toml
├── uv.lock              # Auto-generated
└── .python-version
```

### Legacy Approach (for existing projects)

**Setup:**
```bash
./setup-python-uv.sh
source .venv/bin/activate
```

**Daily workflow:**
```bash
uv pip install package-name
uv pip compile pyproject.toml -o requirements.txt
uv pip sync requirements.txt
python script.py         # Must activate venv first
pytest                   # Must activate venv first
```

**Benefits:**
- Familiar to pip users
- Easier migration from pip
- requirements.txt compatibility

**Project structure:**
```
project/
├── .venv/               # Must activate
├── src/project/
├── tests/
├── pyproject.toml
├── requirements.txt     # Manual generation
└── requirements-dev.txt
```

## Installation Matrix

### New Python Project

```bash
# 1. Create directory
mkdir myproject && cd myproject

# 2. Copy modern boilerplate
cp /path/to/boilerplate/setup-python-uv-modern.sh .
cp /path/to/boilerplate/Makefile.modern.template Makefile
cp /path/to/boilerplate/.gitignore.python.template .gitignore

# 3. Run setup
chmod +x setup-python-uv-modern.sh
./setup-python-uv-modern.sh

# 4. Start coding (no venv activation needed)
uv add requests
uv run python -m myproject
```

### Existing pip-based Project

```bash
# 1. Copy legacy boilerplate
cp /path/to/boilerplate/setup-python-uv.sh .
cp /path/to/boilerplate/Makefile.template Makefile

# 2. Run setup
chmod +x setup-python-uv.sh
./setup-python-uv.sh

# 3. Activate and use
source .venv/bin/activate
python -m myproject

# 4. (Optional) Migrate to modern workflow later
```

### Existing poetry/conda Project

```bash
# 1. Remove poetry/conda files
rm poetry.lock pyproject.toml  # or conda environment files

# 2. Use modern setup
cp /path/to/boilerplate/setup-python-uv-modern.sh .
./setup-python-uv-modern.sh

# 3. Add dependencies
uv add $(cat old-requirements.txt)  # Migrate deps

# 4. Use modern workflow
uv run python -m myproject
```

## Makefile Command Reference

### Modern Makefile

```bash
make help              # Show all commands
make install           # Sync dependencies (uv sync)
make update            # Update all dependencies
make add PKG=requests  # Add dependency
make add-dev PKG=pytest # Add dev dependency
make run               # Run application
make test              # Run tests
make format            # Format with ruff
make lint              # Lint with ruff
make type-check        # Type check with mypy
make check             # Run all checks
make clean             # Clean build artifacts
```

### Legacy Makefile

```bash
make help              # Show all commands
make install           # Install production deps
make install-dev       # Install dev deps
make update            # Update lockfile
make test              # Run tests
make format            # Format with ruff
make lint              # Lint with ruff
make type-check        # Type check with mypy
make check             # Run all checks
make clean             # Clean build artifacts
```

## Common Scenarios

### Scenario 1: Starting Fresh Python Project

**Use:** Modern approach

**Files needed:**
- `setup-python-uv-modern.sh`
- `Makefile.modern.template`
- `.gitignore.python.template`

**Commands:**
```bash
./setup-python-uv-modern.sh
cp Makefile.modern.template Makefile
# Start coding with uv run
```

### Scenario 2: Converting pip Project

**Use:** Legacy approach first, then migrate

**Files needed:**
- `setup-python-uv.sh`
- `Makefile.template`
- `.gitignore.python.template`

**Commands:**
```bash
./setup-python-uv.sh
source .venv/bin/activate
# Test everything works
# Later: migrate to modern approach
```

### Scenario 3: Team Project Migration

**Use:** Phased migration

**Phase 1:** Use legacy approach
```bash
# Everyone uses: uv pip install -r requirements.txt
```

**Phase 2:** Convert to pyproject.toml
```bash
# Add dependencies to pyproject.toml
# Generate: uv pip compile pyproject.toml -o requirements.txt
```

**Phase 3:** Adopt modern workflow
```bash
# Switch to: uv add / uv sync
# Update docs: use "uv run" for all commands
```

## Claude Code Integration

### Project Rules Updated

`.claude/project-rules.md` now includes:
- Mandatory Rust-based uv requirement
- NO pip/conda/poetry allowed
- Modern uv workflow (preferred)
- Legacy uv pip workflow (backward compatibility)
- Python version management
- Dependency management best practices

### CLAUDE.md Updated

`CLAUDE.md` now includes:
- Technology stack (uv as mandatory tool)
- Modern uv commands and workflow
- Project structure for modern projects
- Setup instructions
- Common commands reference

### Assistant Behavior

When Claude Code assists with Python projects:
1. MUST use uv (never pip/conda/poetry)
2. SHOULD prefer modern uv commands for new code
3. SHOULD use `uv run` for executing Python
4. MUST NOT suggest pip/conda/poetry commands
5. SHOULD guide users to modern workflow when possible

## Decision Tree

```
Starting a Python project?
│
├─ Is this a brand new project?
│  ├─ YES → Use setup-python-uv-modern.sh
│  │        Use Makefile.modern.template
│  │        Use modern uv workflow (uv add, uv sync, uv run)
│  │
│  └─ NO → Is it an existing pip project?
│     ├─ YES → Use setup-python-uv.sh (legacy)
│     │        Use Makefile.template
│     │        Plan migration to modern workflow
│     │
│     └─ NO → Is it poetry/conda project?
│        └─ YES → Remove poetry/conda
│                  Use setup-python-uv-modern.sh
│                  Convert dependencies
```

## Boilerplate File Locations

### In This Directory

All boilerplate files are in the current directory:
```
/Users/cmcc/development/band-name-generator/
```

### Copy to New Project

```bash
# Copy modern setup
cp setup-python-uv-modern.sh /path/to/project/
cp Makefile.modern.template /path/to/project/Makefile
cp .gitignore.python.template /path/to/project/.gitignore

# Or copy legacy setup
cp setup-python-uv.sh /path/to/project/
cp Makefile.template /path/to/project/Makefile
```

### Integration with ~/bin/claude-setup-project

The `claude-setup-project` script should:

1. Detect Python project (presence of .py files)
2. Ask user: "New project or existing?"
3. Copy appropriate boilerplate:
   - NEW: Modern files
   - EXISTING: Legacy files
4. Run setup script automatically
5. Update .claude/project-rules.md
6. Update CLAUDE.md

## Maintenance

### Updating Boilerplate Files

When updating these boilerplate files:

1. Update the master copies in this directory
2. Test with a sample project
3. Update version numbers/dates in:
   - UV-RUST-STANDARD.md
   - BOILERPLATE-README.md
   - PYTHON-BOILERPLATE-INDEX.md
4. Commit changes
5. Deploy to projects as needed

### Version History

- **v1.0** (2025-11-11): Initial Rust-based uv standard
  - Modern uv workflow established
  - Legacy uv pip workflow for backward compatibility
  - Comprehensive boilerplate templates
  - Claude Code integration

## Support and Resources

### Documentation
- `UV-RUST-STANDARD.md` - Complete uv standard guide
- `BOILERPLATE-README.md` - Boilerplate usage guide
- `.claude/project-rules.md` - AI assistant rules

### External Resources
- [uv GitHub](https://github.com/astral-sh/uv)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

### Getting Help

1. Check `UV-RUST-STANDARD.md` troubleshooting section
2. Review `BOILERPLATE-README.md` for setup issues
3. Check uv documentation
4. Ask Claude Code for assistance

## Summary

**Standard:** Rust-based uv from Astral is MANDATORY for all Python projects.

**For new projects:** Use modern workflow (`setup-python-uv-modern.sh`)

**For existing projects:** Use legacy workflow (`setup-python-uv.sh`) then migrate

**No exceptions:** NO pip, NO conda, NO poetry

---

Last updated: 2025-11-11
Index version: 1.0
