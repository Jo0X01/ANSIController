#!/usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/env python3
"""
Basic Python Module to control & color & style text in terminal.
Author: JoOx01
Date: 2023-07-30
License: MIT License
"""
from time import sleep
import keyboard
from ANSIController.const import _256_FG,_256_BG,_1ATTR, _RESET, _print
from ANSIController import _ColorsControls, _CursorControls
from ANSIController.tparser import _PARSER


class Terminal(_CursorControls,_ColorsControls):
    __colors = _PARSER._COLORS
    __styles = _PARSER._STYLES
    def __init__(self) -> None:
        super().__init__()
    def get_color(self,char:str,style:int=0,bg:bool=False) -> str:
        return _PARSER.get_color(char,style,bg)
    def get_reset(self) -> str:
        return _RESET
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
