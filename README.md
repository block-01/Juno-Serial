# Juno serial

This is a python application intended to be used to access an [Arm Juno development board](https://developer.arm.com/Tools%20and%20Software/Juno%20Development%20Board)

## Running the application

### Dependancies
- Python
  - Python-venv
  - Python pip
    - pyserial
    - pytest
    - argparse
    - pre-commit
    - pynput
    - termcolor

### Setup

To set up the application run the `setup.sh` script for Linux/MacOS and `setup.bat` for Windows (Work in Progress).

### Usage

To run the application ensure that you are within the `.venv` (can be accessed using the setup scripts) and then execute the command `./main.py` followed by an option, bellow are the applications permitted options:

```term
  -h, --help  show this help message and exit
  --usb0      Connect to serial connection USB0.
  --usb1      Connect to serial connection USB1.
  --usb       Enable the Juno's USB port
  --lsp       Lists out all available serial connections.
```
## ToDo

- Keyboard Input (Top priority)
- Juno USB
- Work on Setup script for Windows
- Documentation
- Tests
