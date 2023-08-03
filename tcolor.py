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
        self._color_code = c[-1][-1]
    def is_that_color(self, char:str) -> bool:
        return char.lower() in self.chars
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
        self._cnames = []
        self._cchars = []
        self._cnums = []
        for c in self.__strings:
            if c.isdigit():
                self._cnums.append(c)
            elif len(c) > 2:
                self._cnames.append(c)
            else:
                self._cchars.append(c)
        self._cnum_re = re.compile(fr"({'|'.join(self._cnums)})")
        self._cnames_re = re.compile(fr"({'|'.join(self._cnames)})", re.IGNORECASE)
        self._cchars_re = re.compile(rf"({'|'.join(self._cchars)})")
        self._cid = re.compile(rf"<({_255Pattern})>")
        self._crgb = re.compile(rf"\(({_255Pattern},{_255Pattern},{_255Pattern})\)")
        self._chash_re = re.compile(rf"((#[0-9a-fA-F]{{6}})|(\({_255Pattern},{_255Pattern},{_255Pattern}\))|(<{_255Pattern}>))")
    def _fix_colors(self,txt:str) -> str:
        _hash_color = self._chash_re.search(txt)
        _new_hash = "\\_####_\\"
        _old_hash = ""
        if _hash_color:
            _old_hash = _hash_color.group(1)# `_random(610)`
            txt = txt.replace(_old_hash,_new_hash)
        _num = self._cnum_re.search(txt)
        if _num:
            _num = str(_num.group(1))
            for _color_ in self._COLORS:
                if _color_.is_that_color(_num):
                    txt = txt.replace(_num,_color_.name)
                    break
        _re = self._cnames_re.search(txt)
        if _re:
            _re = _re.group(1)
            for _color_ in self._COLORS:
                if _color_.is_that_color(_re):
                    txt = txt.replace(_re,str(_color_._color_code))
                    break
        return txt.replace(_new_hash,_old_hash)
    def __color(self,char:str) -> _Color|None:
        for c in self._COLORS:
            if c.is_that_color(char):
                return c
        return None
    def _ex_id(self,txt,bg) -> tuple[int,bool] | None:
        _id = self._cid.search(txt)
        if _id:
            return (int(_id.group(1)),bg)
        return None
    def _ex_rgb(self,txt,bg) -> tuple|None:
        _rgb = self._crgb.search(txt)
        if _rgb:
            return tuple(_rgb.group(1).split(",")+[bg])
        return None
    def _ex_code(self,txt,bg):
        char = self._cchars_re.search(txt)
        return self._get_code(char.group(1) if char else "0",bg)
    def _extract_color(self,text:str,bg:bool) -> tuple:
        _id = self._ex_id(text,bg)
        if _id:
            return _id
        _rgb = self._ex_rgb(text,bg)
        if _rgb:
            return _rgb
        return self._ex_code(text,bg)

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
