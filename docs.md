# ANSIController – Full Documentation

## Introduction
`ANSIController` is a Python library that provides full control over terminal output using ANSI escape codes. It allows developers to move the cursor, colorize text, apply styles, manage progress bars, and create interactive terminal experiences.

This documentation is intended for **developers who want full technical details**, not just a quick overview.

---

## Documentation
- **[ReadMe](README.md)**
- **[Showcase](showcase.md)** – Extended screenshots, demos, and visual examples.


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

Requirements:
- Python 3.x
- Terminal with ANSI escape code support

---

## Quick Start

```python
from ANSIController import Terminal

# Initialize the controller
terminal = Terminal()

# Move the cursor up 3 lines
terminal.move_to_up(steps=3)

# Colorize some text
print(terminal.colorize("[gB]Hello, Green Bold![0]", "[]"))
```

---

## API Reference

### Class: `Terminal`
This is the core class of the library. It contains all terminal control methods.

#### Cursor Control
- **`move_to_up(steps=1, start_line=False)`**  
  Moves the cursor up by `steps` lines. If `start_line=True`, moves to the beginning of the line.

- **`move_to_down(steps=1)`**  
  Moves the cursor down by `steps` lines.

- **`move_to_line(row, col)`**  
  Moves the cursor to a specific `row` and `col`.

- **`move_to_home_postion()`**  
  Moves the cursor to the home position (row 0, column 0).

- **`save_cursor_postion()`** / **`restore_cursor_postion()`**  
  Saves or restores the current cursor position.

- **`hide_cursor()`**, **`show_cursor()`**, **`toggle_cursor()`**  
  Controls the visibility of the cursor.

#### Screen Control
- `clear_screen()` – Clears the entire terminal screen.
- `clear_after_cursor()` – Clears text after the cursor.
- `clear_before_cursor()` – Clears text before the cursor.
- `clear_line()` – Clears the entire line.
- `clear_line_after_cursor()` – Clears text after the cursor in the current line.
- `clear_line_before_cursor()` – Clears text before the cursor in the current line.

#### Colorization & Styling
- **`colorize(text, sep)`**  
  Applies colors and styles to a text string using specified separators.

- **`print_colorize(text, sep)`**  
  Prints directly with applied colors and styles.

#### Progress Bars
- `add_progress(items)` – Adds one or multiple progress bars.
- `update(value=None, progress_key=None, all=False, custom_values=None)` – Updates a progress bar.
- `increase_progress(progress_key=None, all=False)` – Increments progress.
- `set_progress_max_value(value, key=None, all=False)` – Sets max value.
- `set_progress_inc_value(value, key=None, all=False)` – Sets increment value.
- `set_progress_text(text, key=None, all=False)` – Updates progress bar text.
- `print_progress()` – Prints progress bars.
- `is_progress_finish(progress_key=None, all=False)` – Checks if progress is complete.

---

## Color & Style Guide

### Reset Codes
- `[0]`, `[Z]`, `[Reset]` – Resets to default terminal colors and styles.

### Foreground Colors
- `r (red)`, `g (green)`, `y (yellow)`, `b (black)`, `l (blue)`, `m (magenta)`, `c (cyan)`, `w (white)`

### Bright Colors
- `br (bright red)`, `bg (bright green)`, etc.

### Background Colors
- Add `x` or `X` as a prefix, e.g., `[xr]` = red background.

### Styles
- `B (bold)`, `I (italic)`, `U (underline)`, `L (blink)`, `S (strikethrough)`, `R (reverse)`, `H (hidden)`

### RGB & HEX Support
- RGB: `(R,G,B)` e.g. `(213,201,250)`
- HEX: `#FFFFFF`, `#4affa1`

---

## Progress Bar Usage

### Adding Progress Bars
```python
# Add using list
terminal.add_progress([
    "[gB]Download: %b% (%c%/%m%) [0]",
    "[y]Processing: %p% [0]"
])

# Add using dictionary with custom options
terminal.add_progress({
    "download": {
        "txt": "[gB]Downloading: %b% (%c%/%m%) [0]",
        "mx": 100,
        "inc": 5,
        "custom": {"file": "data.zip"}
    }
})
```

### Updating Progress Bars
```python
# Update single progress
terminal.update(value=50, progress_key="download")

# Increment automatically
terminal.increase_progress("download")

# Print progress
terminal.print_progress()
```

### Custom Values in Progress Bars
You can insert dynamic values using `%{key}%` syntax.

Example:
```python
terminal.set_custom_value("status", "Extracting", "download")
terminal.update(custom_values={"status": "Completed"})
```

---

## Common Usage Examples

### Move Cursor
```python
terminal.move_to_up(steps=2)
terminal.move_to_line(row=10, col=5)
```

### Clear Screen
```python
terminal.clear_screen()
terminal.clear_line()
terminal.clear_after_cursor()
```

### Hide and Show Cursor
```python
terminal.hide_cursor()
terminal.show_cursor()
terminal.toggle_cursor()
```

---

## Compatibility & Limitations
- **Windows 7/10/11:** Fully supported
- **Linux:** Mostly supported
- **Termux:** Limited features, some require root

---

## Contributing
Contributions are welcome!  
- Open an [issue](https://github.com/Jo0X01/ANSIController/issues)
- Submit a Pull Request

---

## License
This project is licensed under the **MIT License**.

**Copyright (c) 2023 JoOx01**
