from ANSIController.const import (
    _2ATTR,
    _print,_3ATTR,
    _RESET,
    _COLORS_CODES,_255Pattern,
    re
)
class _Color:
    def __init__(self, c: tuple[int, int, str, list]) -> None:
        self.fg_code, self.bg_code, self.name, self.chars = c
        self.chars += [self.name,str(self.fg_code)]
        self.chars.reverse()
    def is_that_color(self, char) -> bool:
        return char in self.chars
    def get_color_background(self, style: int = 0) -> str:
        return _3ATTR.format(
            s=style,
            fg=self.fg_code,
            bg=self.bg_code
        )
    def get_color(self, style: int = 0) -> str:
        return _2ATTR.format(
            s=style,
            fg=self.fg_code
        )
    def get_reset(self) -> str:
        return _RESET
    def get_code(self) -> tuple[int,int|None]:
        return (self.fg_code,self.bg_code)
    def print_color(self,style: int = 0):
        _print(self.get_color(style))
    def print_color_with_background(self,style:int =0):
        _print(self.get_color_background(style))
    def print_reset(self):
        _print(self.get_reset())
    def test_with_every_style(self,_styles:list):
        s = f"[+] {self.name} \t{self.chars}\n"
        for style in _styles:
            s += f"{style.get_style()}---- [!] {style.get_reset()}{style.mode_name}{style.get_style()}{' '*(15-len(style.mode_name))}"
            s += f"{self.get_color(style.code)}Test{self.get_reset()}\t{style.get_style()}"
            s += f"{self.get_color_background(style.code)}Test{self.get_reset()}\n"
        _print(s)
    def test_with_style(self,style:int=0):
        _print(
            f"[+] {self.name}\t{self.get_color(style)}Test {self.get_color_background(style)}TestBG{_RESET}{','.join(self.chars)}"
        )
    def test(self):
        _print(self.__repr__())
    def __repr__(self) -> str:
        return f"[+] {self.name}{' '*(22-len(self.name))}{self.get_color()}Test {self.get_color_background()}TestBG{self.get_reset()}  {','.join(self.chars)}\n"
class _Colors:
    _COLORS:list[_Color] = [_Color(info) for info in _COLORS_CODES]
    __strings:list[str] = []
    def __init__(self) -> None:
        for _s in self._COLORS:
            self.__strings.extend(_s.chars)
        self.__strings.reverse()
        self._colors = self.__strings
    def __color(self,char:str) -> _Color|None:
        for c in self._COLORS:
            if c.is_that_color(char):
                return c
        return None
    def _extract_color(self,text:str,bg:bool) -> tuple:
        colors_pattern = re.compile(rf"({'|'.join(self.__strings)})")
        _id = re.compile(rf"(\<{_255Pattern})>").search(text)
        if _id:
            _id = _id.group(1)
            return (_id,bg)
        _rgp = re.compile(rf"\(({_255Pattern},{_255Pattern},{_255Pattern})\)").search(text)
        if _rgp:
            rgb = _rgp.group(1)
            return tuple(rgb.split(",")+[bg])
        char = re.search(colors_pattern,text)
        if char:
            char = char.group(1)
        else:
            char = "0"
        return self._get_code(char,bg)
    def _get_code(self,char:str,bg:bool) -> tuple:
        c = self.__color(char)
        if c:
            codes = c.get_code()
            if bg:
                return (codes[0],codes[1])
            return (codes[0],None)
        return (None,None)
    def get_color(self,char:str,style:int=0,bg:bool=False) -> str:
        c = self.__color(char)
        if c:
            return c.get_color_background(style) if bg else c.get_color(style)
        return ""
    def _is_hex_exist(self,box_text:str) -> bool:
        return not re.compile(r'\((\d+,\d+,\d+)\)').search(box_text) == None
