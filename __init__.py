
"""
# ANSI Controller
Basic Python Script to control cursor postion in terminal
and colorize any text in terminal , and add any style to graphic mode in terminal
Note
! This Module work Depends of Terminal Type of support ANSI escape characters or not !
if u face any issue write it

[More Info About ANSI Escape Codes](`https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`)

## Features
------------------------------
`ANSI Controller` Features:
- Move Cursor Right or left or top or down or postion in terminal screen
- Colorize any text u want in terminal
- Change Style of terminal printing text , bold ,italic , etc...

## Tech
------------------------------
# Table of colors & style
- #### if terminal not support colorize the string will just remove from string
- ### Note: Add Custom Values, to string to colorize the output
- #### ID----------: `<{id}>`  from 0 to 255 , `<255>` , `<15>`
- #### RGB---------: `(red_value,green_value,blue_value)` from 0 to 255  , `(213,201,250)`
- #### RGB---------: `#FFFFFF` using hex , `#4affa1`
- #### Background--: `X,x`
- #### Reset-------: `Z,0,reset,Reset`
- #### Colors:
    - [+] `black:`              `b,black,30`
    - [+] `red:`                `r,red,31`
    - [+] `green:`              `g,green,32`
    - [+] `yellow:`             `y,yellow,33`
    - [+] `blue:`               `l,blue,34`
    - [+] `magenta:`            `m,magenta,35`
    - [+] `cyan:`               `c,cyan,36`
    - [+] `white:`              `w,white,37`
    - [+] `default:`            `d,default,39`
    - [+] `bright black:`       `bb,bblack,90`
    - [+] `bright red:`         `br,bred,91`
    - [+] `bright green:`       `bg,bgreen,92`
    - [+] `bright yellow:`      `by,byellow,93`
    - [+] `bright blue:`        `bl,bblue,94`
    - [+] `bright magenta`      `bm,bmagenta,95`
    - [+] `bright cyan:`        `bc,bcyan,96`
    - [+] `bright white:`       `bw,bwhite,97`
- #### Styles:
    - [+] `bold:`               `B,bold,1`
    - [+] `dim:`                `D,dim,2`
    - [+] `italic:`             `I,italic,3`
    - [+] `underline:`          `U,underline,4`
    - [+] `blinking:`           `L,blinking,5`
    - [+] `reverse:`            `R,reverse,7`
    - [+] `hidden:`             `H,hidden,8`
    - [+] `strikethrough:`      `S,strikethrough,9`

## Examples & Usage

> Terminal Execute
### windows
    >>> python -m ANSIController
    >>> ansicontroller
### Linux && Termux
    >>> python3 -m ANSIController
    >>> ansicontroller

> Python Code
    >>> from ANSIController import Terminal  # Import Needed Class
    >>> terminal_control = Terminal()        # Create Object From Class Terminal

# print all styles with test example
>>> Terminal.print_styles()
# print all colors with test example for background too and codes
>>> Terminal.print_colors()
# print all colors & styles with codes
>>> Terminal.print_colors_styles()
# print ids colors background and normal from 0 to 255
>>> Terminal.print_id_colors()
# will print all pervious in same time
>>> Terminal.print_test()
# Try it
>>> Terminal.game()

## to move cursor
    # this will make cursor move to up 3 lines
    >>> terminal_control.move_to_up(steps=3)
    # After move to up 3 lines , cursor will start from 0 postion of line
    >>> terminal_control.move_to_up(steps=3,start_line=True)
    # this will make cursor move to down 1 line
    >>> terminal_control.move_to_down(steps=1)  
    # sometimes terminal not accept to move to up this function will force terminal to move up 1 line
    >>> terminal_control.force_move_to_up() 
    # move cursor to home postion , make cursor in row 0 and col 0
    >>> terminal_control.move_to_home_postion()
    # move cursor to custom postion row {num} col {num} in terminal screen
    # here the cursor will move to row 14 ,column 20
    >>> terminal_control.move_to_line(row=14,col=20) 

## to hide cursor
    # hide cursor , try it
    >>> terminal_control.hide_cursor()
    # show cursor if hidden
    >>> terminal_control.show_cursor()
    # show cursor if hidden and hide if showen
    >>> terminal_control.toggle_cursor()
    # To save cursor postion or restore cursror postion
    >>> terminal_control.save_cursor_postion()   # Save Current Cursor postion row , column
    # Restore Last Saved Cursor postion
    >>> terminal_control.restor_cursor_postion() # cursor will move auto to saved postion

### lets say i want to clear some text from terminal `\r no`
    >>> terminal_control.clear_screen()             # Clear Terminal Screen it close to command `cls` and `clear`
    >>> terminal_control.clear_after_cursor()       # Clear Terminal Screen all text after cursor postion
    >>> terminal_control.clear_before_cursor()      # Clear Terminal Screen all text after cursor postion
    >>> terminal_control.clear_line()               # Clear Current line, of cursor postion row and start from first line
    >>> terminal_control.clear_line_after_cursor()  # Clear Current line, all text after cursor postion in same line
    >>> terminal_control.clear_line_before_cursor() # Clear Current line, all text before cursor postion in same line

### lets say i want to colorize some text
`By Using Concept of - Table of colors & style`
> Using Colors only no styles or background
> Colorize function take : text and seprator
> 
> syntax:
> 
> `sep some_style_codes_or_color_code sep`
> 
> for example `sep is []`
> 
> syntax will be:  `[some_style_codes_or_color_code]`
> 
```python
sep = "[]"
colorize_texts_using_color_char = [
    "[r]This is Red[0]",
    "[g]This is Green[0]",
    "[y]This is Yellow[0]",
    "[b]This is Black[0]",
    "[l]This is Blue[0]",
    "[m]This is Megenta[0]",
    "[c]This is Cyan[0]",
    "[w]This is White[0]",
    "[d]This is default[0]",
    "[bb]This is Bright Black[0]",
    "[br]This is Bright Red[0]",
]
for text in colorize_texts_using_color_char:
    print(terminal_control.colorize(text,sep))
```
> Now Using style only
> 
```python
sep = "[]"
colorize_texts_using_style_char = [
    "[B]This is Bold[0]",
    "[D]This is Dim[0]",
    "[I]This is Italic[0]",
    "[U]This is Underline[0]",
    "[L]This is Blinking[0]",
    "[R]This is reverse[0]",
    "[H]This is Hidden[0]",
    "[S]This is Strikethrogh[0]",
]
for text in colorize_texts_using_style_char:
    print(terminal_control.colorize(text,sep))
```
> Now Using Colors & style
> 
```python
sep = "[]"
colorize_texts_using_style_color_char = [
    "[Br]This is Bold and Red[0]",
    "[Dy]This is Dim and Yellow[0]",
    "[Il]This is Italic and Blue[0]",
    "[Ug]This is Underline and Green[0]",
    "[Lb]This is Blinking and black[0]",
    "[Rbr]This is reverse and Bright Red[0]",
    "[Hby]This is Hidden and Bright Yellow[0]",
    "[Sbc]This is Strikethrogh and Bright Cyan[0]",
]
for text in colorize_texts_using_style_color_char:
    print(terminal_control.colorize(text,sep))
```
> To add Background  just add `X,x` to the block `[xrB]` i want background red and bold style
> 
> Note: you can use `terminal_control.print_colorize` without print
> 
> `[0],[z],[Z],[Reset]` is to reset to default color&style in terminal
________________
## Tests
* ✅ `Windows 11 & 10 & 7`
  * work with no issue
* 👍 `Linux`
  * work but , maybe issue appear
  * Still Work on it
* 🔧 `Termux`
  * Some Features Need Rooted Device
  * Still Work on it
________________
### `if u face any issue dont be shy , say it`
## License

**MIT**
**Copyright (c) 2023 [JoOx01]**
"""
#!/usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/env python3
from time import sleep
import keyboard
from ANSIController.tprogress import _ProgressManage
from ANSIController.controls import (
    _ColorsControls, _CursorControls,
    _print,_RESET,_1ATTR,_256_BG,
    _256_FG,_PARSER
)
from ANSIController.const import _FastColors
class Terminal(_CursorControls,_ColorsControls,_ProgressManage,_FastColors):
    __colors = _PARSER._COLORS
    __styles = _PARSER._STYLES
    def __init__(self) -> None:
        super(_CursorControls,self).__init__()
        super(_ColorsControls,self).__init__()
        super(_ProgressManage,self).__init__()
    def get_color(self,char:str,style:int=0,bg:bool=False) -> str:
        return _PARSER.get_color(char,style,bg)
    def get_reset(self) -> str:
        return _RESET
    def print_multi_colorize(self,text:str|list):
        if isinstance(text,str):
            text = text.split('\n')
        for t in text:
            self.clear_line()
            self.print_colorize(t+'\n') 
    def print_progress(self,leave_end:bool=False):
        txts = self._get_ptexts()
        self.print_multi_colorize(txts)
        if not leave_end:
            self.force_move_to_up(
                len(txts),
                self.is_progress_finish(all=True)
            )
    @staticmethod
    def game(row:int=40,col:int=40,move_steps:int=1):
        control = Terminal()
        for r in range(row):
            print("|"+'-'*col+"|")
        while True:
            try:
                if keyboard.is_pressed('up'):
                    control.move_to_up(move_steps)
                if keyboard.is_pressed("down"):
                    control.move_to_down(move_steps)
                if keyboard.is_pressed("left"):
                    control.move_to_left(move_steps)
                if keyboard.is_pressed("right"):
                    control.move_to_right(move_steps)
                if keyboard.is_pressed("s"):
                    control.save_cursor_postion()
                if keyboard.is_pressed('r'):
                    control.restor_cursor_postion()
                if keyboard.is_pressed('l'):
                    control.clear_line()
                if keyboard.is_pressed("c"):
                    control.save_screen()
                if keyboard.is_pressed("k"):
                    control.restore_screen()
                if keyboard.is_pressed("esc"):
                    return
                sleep(0.1)
            except:
                pass
    @staticmethod
    def print_id_colors():
        _print(f"{_1ATTR.format(s=1)}\n[-] Normal IDs\n{_RESET}")
        for i in range(256):
            _print(f"{_256_FG.format(id=i)}{i} ")
        _print(f"{_1ATTR.format(s=1)}\n[-] Background IDs\n{_RESET}")
        for i in range(256):
            _print(f"{_256_BG.format(id=i)}{i} ")
        _print("="*60+'\n')
        _print(_RESET+'\n')
    @staticmethod
    def print_styles():
        _print(f"{_1ATTR.format(s=1)}\n[-] Test On Styles Only: \n{_RESET}")
        for style in Terminal.__styles:
            style.test()
        _print("="*60+'\n')
        _print(_RESET+'\n')
    @staticmethod
    def print_colors():
        _print(f"{_1ATTR.format(s=1)}\n[-] Test On Colors Only: \n{_RESET}")
        for color in Terminal.__colors:
            color.test()
        _print("="*40+"\n")
        _print(_RESET+'\n')

    @staticmethod
    def print_colors_styles():
        _print(f"{_1ATTR.format(s=1)}\n[-] Test Colors With Styles: \n{_RESET}")
        for color in Terminal.__colors:
            color.test_with_every_style(Terminal.__styles)
        _print("="*40+"\n")
        _print(_RESET+'\n')
    @staticmethod
    def print_test():
        Terminal.print_styles()
        Terminal.print_colors()
        Terminal.print_id_colors()
        Terminal.print_colors_styles()

