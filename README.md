# ANSI Controller
> Basic Python Script to control cursor postion in terminal
> and colorize any text in terminal , and add any style to graphic mode in terminal
<div style="
    color: white;
    background-color: #8B0000;
    padding: 10px;
    alignment: center;
    text-align: center;
">
<b>Note</b><br>
! This Module work Depends of Terminal Type of support ANSI escape characters or not !
<hr>
if u face any issue write it
</div>
<br>

[![PyPi](https://img.shields.io/badge/-PyPi-blue.svg?logo=pypi&labelColor=555555&style=for-the-badge)](https://pypi.org/project/yt-dlp "PyPi") [![License: license](https://img.shields.io/badge/-license-blue.svg?style=for-the-badge)](LICENSE "License")
More Info About ANSI Escape Codes `https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`
## Features
------------------------------
`ANSI Controller` Features:
- Move Cursor Right or left or top or down or postion in terminal screen
- Colorize any text u want in terminal
- Change Style of terminal printing text , bold ,italic , etc...

## Tech
------------------------------

`ANSI Controller` uses a number of open source projects to work properly:
- [keyboard] - pypi module `https://pypi.org/project/keyboard/`
- [More Info About ANSI Escape Codes] `https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`
And of course `ANSI Controller` itself is open source.
 on GitHub.

## Installation
------------------------------

`ANSI Controller` requires [pip](https://pypi.org/) to install.
Install the dependencies and devDependencies and start the script.
```bash
pip install ANSIController
```
# Table of colors & style
- #### if terminal not support colorize the string will just remove from string
- ### Note: Add Custom Values, to string to colorize the output
- #### ID----------: `<{id}>`  from 0 to 255 , `<255>` , `<15>`
- #### RGB---------: `(red_value,green_value,blue_value)` from 0 to 255  , `(213,201,250)`
- #### RGB---------: `#FFFFFF` using hex , `#4affa1`
- #### Background--: `X,x`
- #### Reset-------: `Z,0,reset,Reset`
- #### Colors:
    - [+] `black:`\t            `b,black,30`
    - [+] `red:`\t              `r,red,31`
    - [+] `green:`\t            `g,green,32`
    - [+] `yellow:`\t           `y,yellow,33`
    - [+] `blue:`\t             `l,blue,34`
    - [+] `magenta:`\t          `m,magenta,35`
    - [+] `cyan:`\t             `c,cyan,36`
    - [+] `white:`\t            `w,white,37`
    - [+] `default:`\t          `d,default,39`
    - [+] `bright black:`\t     `bb,bblack,90`
    - [+] `bright red:`\t       `br,bred,91`
    - [+] `bright green:`\t     `bg,bgreen,92`
    - [+] `bright yellow:`\t    `by,byellow,93`
    - [+] `bright blue:`\t      `bl,bblue,94`
    - [+] `bright magenta`\t    `bm,bmagenta,95`
    - [+] `bright cyan:`\t      `bc,bcyan,96`
    - [+] `bright white:`\t     `bw,bwhite,97`
- #### Styles:
    - [+] `bold:`\t             `B,bold,1`
    - [+] `dim:`\t              `D,dim,2`
    - [+] `italic:`\t           `I,italic,3`
    - [+] `underline:`\t        `U,underline,4`
    - [+] `blinking:`\t         `L,blinking,5`
    - [+] `reverse:`\t          `R,reverse,7`
    - [+] `hidden:`\t           `H,hidden,8`
    - [+] `strikethrough:`\t    `S,strikethrough,9`

## Examples & Usage
____________
> Terminal Execute
```shell
python -m ANSIController
```
> Python Code
 ``` python
from ANSIController import Terminal  # Import Needed Class
terminal_control = Terminal()        # Create Object From Class Terminal
```
> To see all test 
```python
# print all styles with test example
Terminal.print_styles()
# print all colors with test example for background too and codes
Terminal.print_colors()
# print all colors & styles with codes
Terminal.print_colors_styles()
# print ids colors background and normal from 0 to 255
Terminal.print_id_colors()
# will print all pervious in same time
Terminal.print_test()
# Try it
Terminal.game()
```
### to move cursor
```python
# this will make cursor move to up 3 lines
terminal_control.move_to_up(steps=3)    

# After move to up 3 lines , cursor will start from 0 postion of line
terminal_control.move_to_up(steps=3,start_line=True)

# this will make cursor move to down 1 line
terminal_control.move_to_down(steps=1)  

# sometimes terminal not accept to move to up this function will force terminal to move up 1 line
terminal_control.force_move_to_up() 

# move cursor to home postion , make cursor in row 0 and col 0
terminal_control.move_to_home_postion()

# move cursor to custom postion row {num} col {num} in terminal screen
# here the cursor will move to row 14 ,column 20
terminal_control.move_to_line(row=14,col=20) 
```
### to hide cursor
```python
# hide cursor , try it
terminal_control.hide_cursor()
# show cursor if hidden
terminal_control.show_cursor()
# show cursor if hidden and hide if showen
terminal_control.toggle_cursor()
```
### To save cursor postion or restore cursror postion
```python
terminal_control.save_cursor_postion()   # Save Current Cursor postion row , column
# Restore Last Saved Cursor postion
terminal_control.restor_cursor_postion() # cursor will move auto to saved postion
```
### lets say i want to clear some text from terminal `\r no`
```python
terminal_control.clear_screen()             # Clear Terminal Screen it close to command `cls` and `clear`
terminal_control.clear_after_cursor()       # Clear Terminal Screen all text after cursor postion
terminal_control.clear_before_cursor()      # Clear Terminal Screen all text after cursor postion
terminal_control.clear_line()               # Clear Current line, of cursor postion row and start from first line
terminal_control.clear_line_after_cursor()  # Clear Current line, all text after cursor postion in same line
terminal_control.clear_line_before_cursor() # Clear Current line, all text before cursor postion in same line
```
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
