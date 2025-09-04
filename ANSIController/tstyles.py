from ANSIController.const import (
    _1ATTR,_print,
    _STYLES_CODES,
    re
)
class _Style:
    def __init__(self, mode: tuple) -> None:
        code, reset_code, mode_name, mode_codes = mode
        self.__code = code
        self.__reset = reset_code
        self.__escape = _1ATTR.format(s=code)
        self.__rescape = _1ATTR.format(s=reset_code)
        self.mode_name = mode_name
        self.mode_codes:list[str] = mode_codes+[mode_name,str(code)]
        self.code = code
    def is_style(self, mode_code: str) -> bool:
        "check if current class equal to mode_code"
        # if isinstance(mode_code,str):
        #     mode_code = mode_code.upper()
        #     if mode_code.isdigit():
        #         mode_code = int(mode_code)
        return mode_code.upper() in self.mode_codes
    def print_style(self) -> None:
        "A function to make anything appear after calling it, so it becomes according to the mode"
        _print(self.__escape)
    def print_reset(self) -> None:
        """A function to reset anything appear after calling it, so it becomes according to the normal mode"""
        _print(self.__rescape)
    def get_style(self) -> str:
        """
            - A function to return the string conversion code to the required mode
            - usage:-
                - print([getMode()]+"__text_changed_to_mode__")
        """
        return self.__escape
    def get_reset(self) -> str:
        """
            - A function to return the string conversion code to the normal mode
            - usage:-
                - print([getResetMode()]+"__text_return_to_normal__")
        """
        return self.__rescape
    def get_reset_code(self) -> int:
        "function to get Reset ESCape Code number of mode"
        return self.__reset
    def get_style_code(self) -> int:
        "function to get ESCape Code number of mode"
        return self.__code
    def test(self):
        "...Display Info About Style, What can do..."
        _print(self.__repr__())
    def __repr__(self) -> str:
        return f"[+] {self.mode_name}{' '*(20-len(self.mode_name))}{self.get_style()}Test{self.get_reset()}  {','.join(self.mode_codes)}\n"
class _Styles:
    _STYLES:list[_Style] = [_Style(info) for info in _STYLES_CODES]
    def __init__(self) -> None:
        self._scodes:list[str] = []
        for _s in self._STYLES:
            self._scodes.extend(_s.mode_codes)
        self.pattern = rf"({'|'.join(self._scodes)})"
        self._snames = []
        self._schars = []
        self._snums = []
        for c in self._scodes:
            if len(c) > 2:
                self._snames.append(c)
            elif c.isdigit():
                self._snums.append(c)
            else:
                self._schars.append(c)
        self._snum_re = re.compile(fr"({'|'.join(self._snums)})")
        self._snames_re = re.compile(fr"({'|'.join(self._snames)})", re.IGNORECASE)
        self._schars_re = re.compile(rf"({'|'.join(self._schars)})")
    def _fix_styles(self,txt:str) -> str:
        _num = self._snum_re.search(txt)
        if _num:
            _num = str(_num.group(1))
            for _style_ in self._STYLES:
                if _style_.is_style(_num):
                    txt = txt.replace(_num,_style_.mode_name)
                    break
        _re = self._snames_re.search(txt)
        if _re:
            _re = _re.group(1)
            txt = txt.replace(_re,_re[0].upper())
        return txt
    def _extract_style(self,text:str) -> tuple:
        p = self._schars_re
        char = p.search(text)
        if char:
            char = char.group(1)
            text = p.sub("",text)
        else:
            char = "0"
        return (text,self._get_style_code_by_char(char))
    def _get_style_code_by_char(self,char:str) -> str | None:
        if isinstance(char,str):
            char = char.upper()
        for s in self._STYLES:
            if s.is_style(char):
                return s.code
        return None
