import os
from ANSIController.tparser import _PARSER
from ANSIController.const import (
    _1ATTR, _256_BG, _256_FG,
    _2ATTR, _3ATTR, _DEFAULT,
    _EARSE, _RESET, _RGB_BG,
    _RGB_FG, _convert_hex_colors,
    _print,re
)


class _CursorControls:
    def __init__(self) -> None:
        self.is_cursor_hide = False
    def __parse_escape(self,char:str):
        _print(_EARSE.format(char))
    def __parse_default(self,char:str):
        _print(_DEFAULT.format(char))
    def move_to_home_postion(self):
        "moves cursor to home position (0,0)"
        self.__parse_escape("H")
    def move_to_line(self, row: int, col: int):
        "#### moves cursor to line {row}, column {col}"
        self.__parse_escape(f"{row};{col}f")
    def move_to_up(self, steps: int = 1, start_line: bool = False):
        """
            ### moves cursor up {steps} lines
            @start_line : after cursor go up , make cursor start from first line
        """
        self.__parse_escape(f"{steps}{'E' if start_line else 'A'}")
    def move_to_down(self, steps: int = 1, start_line: bool = False):
        """
            moves cursor down {steps} lines
            - {start_line} : after cursor go down , make cursor start from first line
        """
        self.__parse_escape(f"{steps}{'F' if start_line else 'B'}")
    def move_to_left(self, steps: int = 1):
        "moves cursor left {steps} lines"
        self.__parse_escape(f"{steps}D")
    def move_to_right(self, steps: int = 1):
        "moves cursor right {steps} lines"
        self.__parse_escape(f"{steps}C")
    def force_move_to_up(self,steps:int=1,clear=False):
        for _ in range(steps):
            self.__parse_default("M")
            if clear:
                self.clear_line()

    def save_cursor_postion(self):
        self.__parse_default("7")
    def restor_cursor_postion(self):
        self.__parse_default("8")

    def hide_cursor(self):
        self.is_cursor_hide = True
        self.__parse_escape("?25l")
    def show_cursor(self):
        self.is_cursor_hide = False
        self.__parse_escape("?25h")
    def toggle_cursor(self):
        self.show_cursor() if self.is_cursor_hide else self.hide_cursor()

    def save_screen(self):
        self.__parse_escape("?47h")
    def restore_screen(self):
        self.__parse_escape("?47l")
    def enable_buffer(self):
        self.__parse_escape("?1049h")
    def disable_buffer(self):
        self.__parse_escape("?1049l")

    # 3J -> dont see the effect
    def clear_screen(self):
        "Clear All Terminal Screen and reset to home postion (0,0)"
        self.__parse_escape("2J")
        # Check the OS and use the appropriate command to clear the screen
        if os.name == 'posix':  # Unix-based systems (Linux and macOS)
            os.system('clear')
        elif os.name == 'nt':   # Windows
            os.system('cls')

    def clear_line_before_cursor(self):
        self.__parse_escape("1K")
    def clear_line_after_cursor(self):
        self.__parse_escape("K")  # 0K
    def clear_before_cursor(self):
        self.__parse_escape("1J")
    def clear_after_cursor(self):
        self.__parse_escape("J")  # 0J
    def clear_line(self):
        self.__parse_escape("2K\r") # type: ignore
    def clear_up_lines(self,steps:int=1):
        self.save_cursor_postion()
        self.force_move_to_up(steps,clear=True)
        self.restor_cursor_postion()

class _ColorsControls:
    def __init__(self) -> None:
        pass

    def __get_colors_escape(self,style:str,colors:tuple) -> str:
        if style == None and all(c is None for c in colors):
            return ""
        if style == 0 and colors == 0:
            return _RESET
        if isinstance(colors[1],bool): # for id color
            r = ""
            if style:
                r += _1ATTR.format(s=style)
            return r + (_256_BG if colors[1] else _256_FG).format(id=colors[0])
        if len(colors) == 4:
            red,green,blue,bg = colors
            return_string = ""
            if style:
                return_string += _1ATTR.format(s=style)
            escape = _RGB_BG if bg else _RGB_FG
            return return_string+escape.format(r=red,g=green,b=blue)
        if style:
            if colors[0]:
                if colors[1]:
                    return _3ATTR.format(s=style,fg=colors[0],bg=colors[1])
                return _2ATTR.format(s=style,fg=colors[0])
            return _1ATTR.format(s=style)
        if colors[1]:
            return _2ATTR.format(s=colors[0],fg=colors[1])
        return _1ATTR.format(s=colors[0])
    def __replace(self,texts:list[str]) -> list[tuple]:
        data = []
        for text in texts:
            if text in ['[z]','[Z]','[0]','[reset]','[Reset]']:
                data.append((text,0,0))
            elif _PARSER._isKnown(text):
                t,style = _PARSER._extract_style(text)
                color = _PARSER._extract_color(t,any(char in "xX" for char in text))
                data.append((text,style,color))
            else:
                data.append(text)
        return data
    def __swap(self,text:str,texts) -> str:
        text,texts = _PARSER._fix_style_colors(text,texts)
        texts = self.__replace(texts)
        for t in texts:
            if isinstance(t,tuple):
                text = text.replace(t[0],_RESET+self.__get_colors_escape(t[1],t[2]),1)
        return text
    def __fix_skip(self,text:str,_found:list[str]) -> tuple[str,list[str]]:
        _manual_replacment:list[str] = []
        for r in _found:
            if '/' in r:
                _found.remove(r)
                _manual_replacment.append(r)
        for m in _manual_replacment:
            text = text.replace(m,m.replace('/',''))
        return (text,_found)
    def colorize(self,text:str,sep:str="[]") -> str:
        """
        ##### @text: text u want to colorize in terminal
        ##### @sep: set special code of colors styles `[]` `!$` `{}` `()` `$$` `??` `}{` and so on
        - ##### if terminal not support colorize the string will just remove from string
        - ### Note: Add This values to string to colorize the output
        - #### Escape------: add char `\\`
            - to escape convertering `{sep}\\ur text\\{sep}` this will print as it is
        - #### ID----------: `<{id}>` -> <255> , <15> from 0 to 255
        - #### RGB---------: `(red_value,green_value,blue_value)` from 0 to 255
        - #### RGB---------: `#FFFFFF` using hex
        - #### Background--: `X,x`
        - #### Reset-------: `Z,0,reset,Reset`
        - #### Codes:
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
        --------------------------------------------------
        ### examples:
        --------------------------------------------------
        - `black` color
            - `>>> colorize("text1[black]text[Z]")`
            - `>>> colorize("[b]text[Z]")`
            - `>>> colorize("[black]text[Z]")`
            - `>>> colorize("[30]text[Z]")`
        --------------------------------------------------
        - `black` color and `bold` style
            - `>>> colorize("[black;bold]text[Z]")`
            - `>>> colorize("[b;B]text[Z]")`
            - `>>> colorize("[bB]text[Z]")`
            - `>>> colorize("[301]text[0]")`
        --------------------------------------------------
        - `black` color and `bold` style and Background
            - `>>> colorize("[black;bold;X]text[Z]")`
            - `>>> colorize("[b;B;x]text[0]")`
            - `>>> colorize("[bBX]text[0]")`
            - `>>> colorize("[301x]text[0]")`
        --------------------------------------------------
        """
        fsep,esep = sep,sep
        if len(sep) == 2:
            fsep,esep = sep[0],sep[1]
        fsep = re.escape(fsep)
        esep = re.escape(esep)
        text = _convert_hex_colors(text)
        _re = fr"{fsep}[^{fsep}{esep}].*?{esep}"
        _found = re.compile(rf"({_re})").findall(text)
        text,_found = self.__fix_skip(text,_found)
        return self.__swap(text,_found)
    def print_colorize(self,text:str,sep:str="[]") -> None:
        _print(self.colorize("[d]"+text+"[d]",sep))
