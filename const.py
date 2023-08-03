
# escape char in dfrnt numbers system
import random
import re
import string
from sys import stdout


_CSI = "\x9B" # ESC [
_DCS = "\x90" # ESC P
_OSC = "\x9D" # ESC ]
_OCT = "\033"
_HEX = "\x1b"
_DEC = "\27"

# constant vars to use escape chars
_ESC = _HEX or _OCT or _DEC
_DEFAULT        = f"{_ESC}{{}}"
_EARSE          = f"{_ESC}[{{}}"
_1ATTR          = f"{_ESC}[{{s}}m"
_2ATTR          = f"{_ESC}[{{s}};{{fg}}m"
_3ATTR          = f"{_ESC}[{{s}};{{fg}};{{bg}}m"
_RGB_BG         = f"{_ESC}[48;2;{{r}};{{g}};{{b}}m"
_RGB_FG         = f"{_ESC}[38;2;{{r}};{{g}};{{b}}m"
_256_BG         = f"{_ESC}[48;5;{{id}}m"
_256_FG         = f"{_ESC}[38;5;{{id}}m"
_RESET          = f"{_ESC}[0m"

# pattern regex
_255Pattern = r"\b(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b" or r"?:25[0-5]|2[0-4]\d|[01]?\d{1,2}"
# colors and modes terminal
_STYLES_CODES = [
    # code , reset code , mode name , mode chars
    (1, 22, "bold", ['B']),
    (2, 22, "dim", ["D"]),
    (3, 23, "italic", ['I']),
    (4, 24, "underline", ['U']),
    (5, 25, "blinking", ['L']),
    (7, 27, "reverse", ['R']),
    (8, 28, "hidden", ['H']),
    (9, 29, "strikethrough", ['S']),
]
_COLORS_CODES = [
    # foreground color , background color , name , codes
    (30, 40, "black", ["b"]),
    (31, 41, "red", ["r"]),
    (32, 42, "green", ["g"]),
    (33, 43, "yellow", ["y"]),
    (34, 44, "blue", ["l"]),
    (35, 45, "magenta", ["m"]),
    (36, 46, "cyan", ["c"]),
    (37, 47, "white", ["w"]),
    (39, 49, "default", ["d"]),
    (90, 100, "brightblack", ["bb","bblack"]),
    (91, 101, "brightred", ["br","bred"]),
    (92, 102, "brightgreen", ["bg",'bgreen']),
    (93, 103, "brightyellow", ["by",'byellow']),
    (94, 104, "brightblue", ["bl",'bblue']),
    (95, 105, "brightmagenta", ["bm",'bmagenta']),
    (96, 106, "brightcyan", ["bc",'bcyan']),
    (97, 107, "brightwhite", ["bw",'bwight']),
]

def _print(data):
    stdout.write(data)
    stdout.flush()

def hex_to_rgb(hex_code:str):
    hex_code = hex_code.lstrip('#')  # Remove '#' if present
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def _convert_hex_colors(text:str) -> str:
    for hex in re.compile(r'(#[a-fA-F0-9]{1,6})').findall(text):
        r,g,b = hex_to_rgb(hex)
        text = text.replace(hex,f"({r},{g},{b})")
    return text
def _convert_time(sec: int, format: str = "h:m:s") -> str:
    sec = int(sec)
    hours = sec // 3600
    remaining_seconds = sec % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    if format == "h:m:s":
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    elif format == "h:m":
        return f"{hours:02d}:{minutes:02d}"
    elif format == "m:s":
        return f"{minutes:02d}:{seconds:02d}"
    elif format == "h":
        return f"{hours:02d}"
    return ""
