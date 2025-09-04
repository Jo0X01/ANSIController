![App Icon](ANSIController.ico)

# ANSI Controller

![PyPi](https://img.shields.io/badge/-PyPi-blue.svg?logo=pypi&labelColor=555555&style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)

An Python module to control cursor movement, apply colors, and style text in the terminal using ANSI escape codes.

---

## Features
- Cursor control: move up, down, left, right, or to specific coordinates.
- Text colorization: standard, bright, RGB, and HEX colors.
- Styling: **bold**, *italic*, underline, blink, reverse, hidden, strikethrough.
- Customizable progress bars (multi-progress supported).
- Terminal clearing options (partial or full).
- Cross-platform: Windows, Linux, Termux (limited features).

---

## Installation
### Windows
```bash
pip install --upgrade ANSIController
```

### Linux & Termux
```bash
pip3 install --upgrade ANSIController
```

---

## Quick Start
```python
from ANSIController import Terminal

terminal = Terminal()

# Move cursor up 3 lines
terminal.move_to_up(steps=3)

# Colorize text
text = "[rB]Hello, Red Bold![0]"
print(terminal.colorize(text, "[]"))

# Hide and show cursor
terminal.hide_cursor()
terminal.show_cursor()
```

---

## Documentation
- **[Full Documentation](docs.md)** – Detailed API reference and usage.
- **[Showcase](showcase.md)** – Extended screenshots, demos, and visual examples.

---

## Screenshots
Essential visuals for quick reference:

![Progress Bar](ANSIController/tests/test_progress.gif)

---

## Notes
- Works only in terminals supporting **ANSI escape codes**.
- Some Termux features may require root privileges.
- Designed for scripting, automation, and learning.

---

## License
This project is licensed under the **MIT License**.

**Copyright (c) 2023 JoOx01**

---

## Contributing & Issues
Found a bug? Have a feature request? Open an
[issue](https://github.com/Jo0X01/ANSIController/issues) or submit a PR!

---

## Tests
- **Windows 7/10/11:** Fully supported
- **Linux:** Mostly supported
- **Termux:** Limited features, some require root access
