# Custom Command-Line Interface

This project implements a customizable command-line interface (CLI) with extensible commands and modules.

## Features

- Customizable command prompt
- Extensible command system
- Support for nested commands and arguments
- Module system for organizing and managing commands
- Built-in networking and system commands
- Cross-platform compatibility (Windows, macOS, Linux)

## Core Files

- `main.py`: Entry point of the application
- `console.py`: Implements the Console class for handling user input
- `command.py`: Implements the Command class for managing and executing commands
- `check.py`: Defines the initial set of commands
- `utils.py`: Contains utility functions for command processing
- `userUtils.py`: Provides user-facing utility functions
- `module.py`: Implements the module system for organizing commands
- `color.py`: Handles colored output (not provided in the snippets)

## Usage

1. Ensure you have Python installed on your system.
2. Install required dependencies:
   ```
   pip install colorama
   ```
3. Run the application:
   ```
   python main.py
   ```

## Adding New Commands

To add new commands, modify the `entries` function in `check.py`:

```python
def entries(console, commands):
cmd = {
"new_command": lambda path, args: your_function(args),
# Add more commands here
}
return [cmd, {}]
```

## Module System

The project includes a module system for organizing commands. Use the `Modules` class in `module.py` to add or remove command modules.

## Configuration

The `default.wcons` file contains JSON configuration for the project:

```json
{
"author": "Rabin",
"version": "1.0",
"filename": "check.py"
}
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
MIT


