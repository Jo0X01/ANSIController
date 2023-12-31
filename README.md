```sh

#         d8888 888b    888  .d8888b. 8888888                                              
#        d88888 8888b   888 d88P  Y88b  888                                                
#       d88P888 88888b  888 Y88b.       888                                                
#      d88P 888 888Y88b 888  "Y888b.    888                                                
#     d88P  888 888 Y88b888     "Y88b.  888                                                
#    d88P   888 888  Y88888       "888  888                                                
#   d8888888888 888   Y8888 Y88b  d88P  888                                                
#  d88P     888 888    Y888  "Y8888P" 8888888                                              
#                                                                                          
#                                                                                          
#                                                                                          
#              .d8888b.                    888                    888 888                  
#             d88P  Y88b                   888                    888 888                  
#             888    888                   888                    888 888                  
#             888         .d88b.  88888b.  888888 888d888 .d88b.  888 888  .d88b.  888d888 
#             888        d88""88b 888 "88b 888    888P"  d88""88b 888 888 d8P  Y8b 888P"   
#             888    888 888  888 888  888 888    888    888  888 888 888 88888888 888     
#             Y88b  d88P Y88..88P 888  888 Y88b.  888    Y88..88P 888 888 Y8b.     888     
#              "Y8888P"   "Y88P"  888  888  "Y888 888     "Y88P"  888 888  "Y8888  888     
#                                                                                         
```
# ANSI Controller
> Basic Python Script to control cursor postion in terminal
> and colorize any text in terminal , add any style to graphic mode in terminal

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

# Note:
> #### The Goal of writing this script is to make it easier to control the terminal by simply writing the name of the color or the name of the style of the text or moving the cursor by calling a function or deleting the text in the window, use it to learn how much it will make it easier for you if you are always using the command window


[![PyPi](https://img.shields.io/badge/-PyPi-blue.svg?logo=pypi&labelColor=555555&style=for-the-badge)](https://pypi.org/project/ANSIController "PyPi") [![License: license](https://img.shields.io/badge/-license-blue.svg?style=for-the-badge)](LICENSE "License")

[More Info About ANSI Escape Codes](`https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`)

## Tool Snap
_______________
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/tool.png)

## Features
------------------------------
`ANSI Controller` Features:
- Move Cursor Right or left or top or down or postion in terminal screen
- Colorize any text u want in terminal
- Change Style of terminal printing text , bold ,italic , etc...
- MultiProgress in same time
## Tech
------------------------------
`ANSI Controller` uses a number of open source projects to work properly:
- [keyboard] - pypi module `https://pypi.org/project/keyboard/`
- `ANSI Controller` itself is open source on GitHub.
- `More Info About ANSI Escape Codes: `https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape
## Installation
------------------------------

`ANSI Controller` requires [pip](https://pypi.org/) to install.
Install the dependencies and devDependencies and start the script.
### Windows
```bash
pip install ANSIController
```
### Linux && Termux
```bash
pip3 install ANSIController
```
# Table of colors & style
- #### if terminal not support colorize the string will just remove from string
- ### Note: Add Custom Values, to string to colorize the output
> - ### [ID Colors](https://robotmoon.com/256-colors/): `<{id}>`  from 0 to 255 , `<255>` , `<15>`

> - ### [RGB Colors](https://www.rapidtables.com/web/color/RGB_Color.html): `(red_value,green_value,blue_value)` from 0 to 255  , `(213,201,250)`
> - ### [Hex RGB](https://www.rapidtables.com/web/color/RGB_Color.html): `#FFFFFF` using hex , `#4affa1`

- #### Background: `X,x`
- #### Reset: `Z,0,reset,Reset`
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
- #### ProgressBar: add `%{char}%`
    - [+] `c:`                  `current progress value`
    - [+] `m:`                  `max progress value`
    - [+] `p:`                  `percent progress value`
    - [+] `b:`                  `bar progress value`
    - [+] `f:`                  `print full bar with all info`
    - [+] `e:` `Elapsed Time`
    - [+] `r:` `Remaining Time`
    - [+] `s:` `Speed`
    - [+]  `your_custom_key:`    `your_custom_value`
- #### More Control in ProgressBar:
    - [+] `txt:`                `key of string value inside`
    - [+] `mx:`                 `max value default is 100`
    - [+] `inc:`                `increamnt value defualt is 1`
    - [+] `bopen:` `bar open char default '|'`
    - [+] `bfill:` `bar filled char default '█'`
    - [+] `bafill:` `bar after filled char default ''`
    - [+] `bempty:` `bar empty char default ' '`
    - [+] `bclose:` `bar close char default ' '`
    - [+] `custom:`             `dict object with custom keys`
## Examples & Usage
____________
> Terminal Execute
### windows
```shell
python -m ANSIController
```
> OR
```shell
ansicontroller
```
### Linux && Termux
```shell
python3 -m ANSIController
```
> OR
```shell
ansicontroller
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
## Output:
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_styles.png)
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_colors.png)
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_ids.png)
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
## Output:
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_colors_out.png)
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
## Output:
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_styles_out.png)
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
## Output:
![Alt Text](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_colors_style_out.png)
> To add Background  just add `X,x` to the block `[xrB]` i want background red and bold style
> 
> Note: you can use `terminal_control.print_colorize` without print
> 
> `[0],[z],[Z],[Reset]` is to reset to default color&style in terminal
> 
> 
### - Using multiprogressbar
```python
# add_progress: take list of text
# take too dict
#example with list
terminal_control.add_progress([
    "[rB]test1[0]",
    "[w]test2[0]",
    "[cI]test3[0]",
    "[yD]test4[0]",
])
# example with dict
# take `progress_name`` to access later
# `txt` key is the progress text
terminal_control.add_progress({
    "progress1":{"txt": "[rB]test1[0]"},
    "progress2":{"txt": "[w]test2[0]"},
    "progress3":{"txt": "[cI]test3[0]"},
    "progress4":{"txt": "[yD]test4[0]"},
})
# now if i want to add progress value and update values
#example with list
# access by index
terminal_control.add_progress([
    "[rB]test1: (%c%/%m%)[0]",
    "[w]test2: %b% (%c%/%m%)[0]",
    "[cI]test3: %b% %p% (%c%/%m%)[0]",
    "[yD]test4: %f% [0]",
])
#example with more control dict
terminal_control.add_progress({
    "progress1":{
        "txt": "[rB]test1: (%c%/%m%) - (%key1%,%key2%,%status_test%)[0]",
        "mx":200,
        "inc":5,
        "custom":{
            "key1":10,
            "key2":"test",
            "status_test":"Good"
        }
    },
    # sometimes no need for `mx` or `inc`
    "progress2":{
        "txt": "[w]test2: %b% (%c%/%m%)- (%key1%,%key2%)[0]",
        "custom":{
            "key1":10,
            "key2":"test",
            "status_test":"Good"
        }
    },
    'progress_key1'|progress_key_integar:{
        'txt':string...,
        'mx':100,
        'inc':1,
        'custom':{},
        'bopen':'|',
        'bfill':'█',
        'bafill':'',
        'bempty':' '
        'bclose':'|',
    }
})

#----------------------------------------
# now to update progress bar values

# progress_key = `if list will be index`
# progress_key = `if dict will be name`
# `all` argument mean if u want to change in all texts
# default of all is False

# to change max value of custom texts
terminal_control.set_progress_max_value(150,"progress_key")
terminal_control.set_progress_max_value(150,all=True)

# to change auto increment value of custom texts
terminal_control.set_progress_inc_value(5,"progress_key")
terminal_control.set_progress_inc_value(5,all=True)

# to change text value of custom texts
terminal_control.set_progress_text("[rD]This is Text[0]","progress_key")
terminal_control.set_progress_text("[rD]This is Text[0]",all=True)

# to change or add custom value of custom texts
terminal_control.set_custom_value("key1","value1","progress_key")
terminal_control.set_custom_value("key1","value1",all=True)

#----------------------------------------
# now to update progress value

# this function more control in update
terminal_control.update(
    value = 13, # if no progress value, leave it
    progress_key="progress_key", # if no all, leave it
    all=True or False,
    custom_values={
        "key1":"value1",
        "key2":"value2"
    }
)
# if u want to auto update using `inc` value just call this
terminal_control.increase_progress("progress_key")
terminal_control.increase_progress(all=True)

#----------------------------------------
# now to print & check progress value
# to print all progress text with colorize mode
terminal_control.print_progress()
# to check is progress finish or not
terminal_control.is_progress_finish("progress_key")
terminal_control.is_progress_finish(all=True)
```
## Output:
![ProgressBar GIF](https://raw.githubusercontent.com/Jo0X01/ANSIController/main/tests/test_progress.gif)
## Ref
________________
- https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape
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

**MIT License**
**Copyright (c) 2023 [JoOx01]**

`Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.`


