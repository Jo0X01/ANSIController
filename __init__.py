## more info `https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#escape`

__author__ = 'JoOx01'
__desc__ = """Basic Python Module to control & color & style text in terminal"""
import sys
from time import sleep
import keyboard
from ANSIController.const import _256_FG,_256_BG,_1ATTR, _RESET, _print
from ANSIController.controls import _ColorsControls, _CursorControls
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
            print("|"+'-'*col)
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

def main():
    t = Terminal()
    while True:
        _print(f"""-----------------------
{t.get_color('green',5)}{__desc__}{t.get_reset()}
-----------------------{t.get_color('yellow',5)}
╔═══╦═╗░╔╦═══╦══╦══╗
║╔═╗║║╚╗║║╔═╗╠╣╠╩╣╠╝
║║░║║╔╗╚╝║╚══╗║║░║║░
║╚═╝║║╚╗║╠══╗║║║░║║░
║╔═╗║║░║║║╚═╝╠╣╠╦╣╠╗
╚╝░╚╩╝░╚═╩═══╩══╩══╝{t.get_reset()}
-----------------------
by {t.get_color('red',1)}{__author__}{t.get_reset()}
-----------------------
[1] Print ALL Colors
[2] Print ALL Styles
[3] Colors With Styles
[4] Print All
[5] X O   # soon 
[6] Snake # soon
[7] Move Game
[8] Colorize Text
[9] Clear Screen
[-1] End
-----------------------
>>> 
-----------------------""")
        t.force_move_to_up()
        t.move_to_left(50)
        # t.move_to_up(start_line=True)
        choice = str(input(">>> "))
        if choice == "1":
            t.print_colors()
            input()
        if choice == "2":
            t.print_styles()
            input()
        if choice == "3":
            t.print_colors_styles()
            input()
        if choice == "4":
            t.print_test()
            input()
        if choice == "7":
            t.game(100,100,2)
        if choice == "8":
            text = str(input("Text `[your_color_code]`: "))
            t.print_colorize(text)
            input()
        if choice == "9":
            t.clear_screen()
        if choice == '-1':
            _print("Thx For Using Bye\n")
            break
if __name__ == '__main__':
    try:
        main()
    except:
        pass
