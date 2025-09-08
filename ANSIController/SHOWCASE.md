# ANSIController Showcase

This file contains extended screenshots, demos, and visual examples for **ANSIController**.

---

## Screenshots

### Tool Snapshot
![Tool](ANSIController/tests/tool.png)

### Colors Output
![Colors Output](ANSIController/tests/test_colors_out.png)

### Styles Output
![Styles Output](ANSIController/tests/test_styles_out.png)

### ID Colors
![IDs](ANSIController/tests/test_ids.png)

### Progress Bar Animation
![Progress](ANSIController/tests/test_progress.gif)

---

## Combined Color & Style Examples

```python
sep = "[]"
examples = [
    "[Br]Bold and Red[0]",
    "[Dy]Dim and Yellow[0]",
    "[Il]Italic and Blue[0]",
    "[Ug]Underline and Green[0]",
    "[Lb]Blinking Black[0]",
    "[Rbr]Reverse Bright Red[0]",
    "[Hby]Hidden Bright Yellow[0]",
    "[Sbc]Strikethrough Bright Cyan[0]",
]
for e in examples:
    print(terminal.colorize(e, sep))
```

---

## Multi-Progress Bar Example

```python
terminal.add_progress({
    "download": {
        "txt": "[gB]Downloading: %b% (%c%/%m%) [0]",
        "mx": 100,
        "inc": 5
    },
    "process": {
        "txt": "[y]Processing: %p% [0]",
    }
})

# Update in loop
for i in range(0, 101, 5):
    terminal.update(value=i, progress_key="download")
    terminal.update(value=i, progress_key="process")
    terminal.print_progress()
```

---

## Notes 
- This file complements the main **README.md** and **DOCS.md** files.
