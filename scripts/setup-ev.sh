#!/bin/bash

# --- Configuration ---
PROJECT_NAME="rust-uv-project"
VENV_DIR=".venv"
# List of required Python packages
PYTHON_PACKAGES=(
    "requests"
    "pydantic"
    "fastapi"
)
# --- End Configuration ---

echo " Starting project setup for: $PROJECT_NAME"

# 1. Create the main project directory
if [ ! -d "$PROJECT_NAME" ]; then
    mkdir "$PROJECT_NAME"
    echo " Created project directory: $PROJECT_NAME"
else
    echo "️ Project directory $PROJECT_NAME already exists. Proceeding..."
fi

cd "$PROJECT_NAME"

# 2. Create the virtual environment using 'uv venv'
echo -e "\n️ Creating virtual environment using uv..."
# 'uv venv' creates the venv in the specified directory (e.g., .venv)
if uv venv "$VENV_DIR"; then
    echo " Virtual environment created successfully in $VENV_DIR"
else
    echo " Error creating virtual environment. Ensure 'uv' is installed and on your PATH."
    exit 1
fi

# 3. Install required packages using 'uv pip install'
echo -e "\n Installing Python dependencies into the virtual environment..."

# The '-p' flag tells 'uv' to use the Python interpreter inside the specified venv
if uv pip install -p "$VENV_DIR" "${PYTHON_PACKAGES[@]}"; then
    echo -e "\n Successfully installed all required packages:"
    for package in "${PYTHON_PACKAGES[@]}"; do
        echo "   - $package"
    done
else
    echo " Error installing packages. Installation failed."
    exit 1
fi

# 4. Activation Instructions (for user reference)
# Determine the activation script path based on the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    # Linux/macOS (Bash/Zsh)
    ACTIVATE_CMD="source $VENV_DIR/bin/activate"
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows (WSL, Git Bash, or Command Prompt/PowerShell)
    # Note: On Windows cmd/PowerShell, the command is different, but we'll show the common path
    ACTIVATE_CMD=".\\$VENV_DIR\\Scripts\\activate"
fi

echo -e "\n--- Setup Complete ---"
echo "To begin working on your project, run the following command to activate the virtual environment:"
echo "️ **$ACTIVATE_CMD**"
echo "----------------------"

# Optional: List installed packages to confirm
echo -e "\nInstalled packages (via uv pip list):"
"$VENV_DIR/bin/uv" pip list
