import time,re
from typing import Any
from ANSIController.const import _convert_time,_convert_bytes,_ANSIErrors


class _Progress:
    def __init__(
        self,
        text: str,
        mx: int = 0,
        key:str|int = 0,
        increase_value: int = 1,
        custom_values: dict = {},
        bar_open:str|None = None,
        bar_fill:str|None = None,
        bar_after_fill: str|None = None,
        bar_space:str|None = None,
        bar_close: str|None = None,
        sunit:str|None = None,
        download: bool|None=None
    ) -> None:
        self.key = str(key)
        self.max_value = mx
        self.min_value = 0
        self.cur_value = 0
        self.__text = text
        self.increase_value = increase_value
        self._custom_table = custom_values
        self._start_time = time.time()
        self.___re_keys_g1 = re.compile(r"(\%[bcefmprs]{1,7}\%)",2)
        self.___re_keys_big = re.compile(r"(\%\$.*?\$\%)",2)
        self.___re_remove = re.compile(r"([\%\$|\$\%])")
        self.set_bar_values(
            bar_open,
            bar_close,
            bar_fill,
            bar_after_fill,
            bar_space,
            sunit,
            download
        )
        self._loading_chars = ['-','\\','|','/']
        self._loading_next = -1
    def is_finish(self) -> bool:
        if self.max_value <= 0:
            return True
        if self.cur_value >= self.max_value:
            self.cur_value = self.max_value
            return True
        return False
    def update(self, current_value: int, custom_values: dict = {}):
        self.cur_value = current_value
        self._custom_table |= custom_values
        self.is_finish()

    def increase(self):
        self.cur_value += self.increase_value
        self.is_finish()

    def update_text(self, text: str):
        self.__text = text

    def set_custom_value(self, key, value):
        if key in self._custom_table:
            self._custom_table[key] = value
    def set_loading_chars(self,loading_chars:list[str]):
        self._loading_chars = loading_chars
    def set_bar_values(
        self,
        bar_open: str | None = None,
        bar_close: str | None = None,
        bar_fill: str | None = None,
        bar_after_fill: str|None = None,
        bar_space: str | None = None,
        sunit:str|None = None,
        download: bool|None=None
    ):
        self.bar_open = bar_open if bar_open else '|'
        self.bar_end = bar_close if bar_close else '|'
        self.bar_fill = bar_fill if bar_fill else "█"
        self.bar_space = bar_space if bar_space else " "
        self.bar_after_fill = bar_after_fill if bar_after_fill else ''
        self.sunit = sunit if sunit else "Unit/s"
        self.download = download if download else False
    @property
    def current_value(self) -> int:
        return self.cur_value or 1
    @property
    def maxmum_value(self) -> int:
        return self.max_value if self.max_value > 0 else 1
    @property
    def percent(self) -> float:
        return float((self.current_value / self.maxmum_value) * 100)

    @property
    def percent_str(self) -> str:
        fp = "{:.2f}".format(self.percent)
        if fp.endswith(".00"):
            fp = "{:.0f}".format(self.percent)
        return fp

    @property
    def elapsed_time(self) -> int:
        return int(time.time() - self._start_time)

    @property
    def elapsed_time_str(self) -> str:
        return _convert_time(self.elapsed_time)

    @property
    def remaining_time(self) -> int:
        telapsed = time.time() - self._start_time
        testimated = (telapsed/self.current_value) * self.maxmum_value
        return int(testimated-telapsed)

    @property
    def remaining_time_str(self) -> str:
        return _convert_time(self.remaining_time)
    @property
    def speed(self) -> int:
        return int(self.current_value / (self.elapsed_time or 1))
    @property
    def speed_str(self) -> str:
        return _convert_bytes(self.speed)+"/s" if self.download else f"{self.speed:.2f}{self.sunit}"
    @property
    def bar(self) -> str:
        # |█████████████████
        filled_chars = round((self.percent / 100) * 20)
        empty_chars = 20 - filled_chars
        return (
            self.bar_open +
            self.bar_fill * filled_chars +
            self.bar_after_fill +
            self.bar_space * empty_chars +
            f"{self.bar_end}"
        )
    @property
    def full_bar(self) -> str:
        return self.bar + f" ({self.cur_value})"
    def set_max_value(self, mx: int):
        self.max_value = mx

    def set_increase_value(self, value: int):
        self.increase_value = value
    def ___lower(self,text:str) -> str:
        def __lower(match):
            return match.group(1).lower()
        return self.___re_keys_g1.sub(__lower,text)
    def ___extract_chars___(self,text:str) -> tuple[str,list[str]]: 
        text = self.___lower(text)
        return (
            text,
            [_c for _c in self.___re_keys_g1.findall(text)]
        )
    def ___ff_converter___(self,char:str) -> str:
        char = char.replace("%",'')
        if char.startswith("f"):
            _nc = "%f%"
            if char.startswith("ff"):
                _nc = "%ff%"
            char = char.replace("f",'')
            _nc += " " +" - ".join([f"%{_c}%" for _c in char])
            return _nc
        return f"%{char}%"
    def ___filtrize_and_fix_text___(self,text:str,_real_chars:list[str]):
        for char in _real_chars:
            text = text.replace(char,self.___ff_converter___(char))
        return text
    def ___sort_short_chars___(self,text:str) -> str:
        def replace(match):
            return f'%{match.group(1)}%'
        _chars:list[str] = self.___re_keys_big.findall(text)
        for _pchar in _chars:
            chars = re.compile(rf"(?<!\[[^\]])\b({'|'.join(self._all_chars)})\b(?![^\[]*\])",2)#.findall(_pchar)
            text = text.replace(_pchar,chars.sub(replace,_pchar).replace("%$",''))
        return text
    def ___clear_any_chars___(self,text:str) -> str:
        return self.___re_remove.sub("",text).strip()
    @property
    def table_chars(self) -> list[str]:
        return list(self.table.keys())
    @property
    def _lower_default_chars(self) -> list[str]:
        return [_c.lower() for _c in self._default_table.keys()]
    @property
    def _upper_default_chars(self) -> list[str]:
        return [_c.upper() for _c in self._default_table.keys()]
    @property
    def _default_chars(self) -> list[str]:
        return self._lower_default_chars+self._upper_default_chars
    @property
    def _all_chars(self) -> list[str]:
        return self._default_chars + list(self._custom_table.keys())
    @property
    def _circle_turn(self) -> str:
        self._loading_next += 1
        if self._loading_next >= len(self._loading_chars):
            self._loading_next = 0
        char= self._loading_chars[self._loading_next]
        if not char:
            char = self._loading_chars[0]
            self._loading_next = 0
        return char
    @property
    def _default_table(self) -> dict:
        _d = {
            "l"  : self._circle_turn,
            "c"  : self.cur_value,
            "cf" : _convert_bytes(self.cur_value),
            "m"  : self.max_value,
            "mf" : _convert_bytes(self.max_value),
            "p"  : self.percent_str,
            "pp" : self.percent_str+"%",
            "b"  : self.bar,
            "fb" : self.full_bar,
            "r"  : self.remaining_time_str,
            "e"  : self.elapsed_time_str,
            "s"  : self.speed_str
        }
        return _d | {
            "f"  : f"{_d['b']} {_d['pp']} - ({_d['c']}/{_d['m']})",
            "ff" : f"{_d['b']} {_d['pp']} - ({_d['cf']}/{_d['mf']})"
        }
    @property
    def table(self):
        return self._custom_table | self._default_table
    @property
    def text(self) -> str:
        text = self.__text
        text = self.___sort_short_chars___(text)
        text,_real_chars = self.___extract_chars___(text)
        text = self.___filtrize_and_fix_text___(text,_real_chars)
        for key, value in self.table.items():
            text = text.replace(f"%{key}%", str(value))
        return text
class _ProgressManage:
    def ___isinstance(self,value,types) -> bool:
        return isinstance(value, types[0]) and all(isinstance(i, types[1]) for i in value)
    def ___fix_text_progress(self,text:Any) -> dict[str|int,dict] | list: # type: ignore
        if self.___isinstance(text,(list,str)):
            return text # type: ignore
        if isinstance(text,str):
            return [text]
        if self.___isinstance(text,(dict,str)):
            return {1:text} # type: ignore
        if self.___isinstance(text,(list,dict)):
            _key = 1
            _text = {}
            for _dict in text:
                _text[_key] = _dict
                _key+=1
            text = _text
            return text
        raise ValueError("Progress Texts Too Bad")
    def ___gen_key___(self,key:str) -> str:
        _keys = re.compile(rf"({key}_\d+)").findall(",".join(self._repeated_keys))
        if _keys:
            _keys.sort(reverse=True)
            return f"{key}_{int(_keys[0][-1])+1}"
        if key in self._repeated_keys:
            return f"{key}_1"
        return key
    def ___fix_repeated_key(self,key:int|str) -> str|int:
        key = self._fix_key(key,False,_str=True)
        key = self.___gen_key___(key)
        self._repeated_keys.append(key)
        self._repeated_keys.sort()
        return key
    def __init__(self) -> None:
        self.reset_progress()

    def reset_progress(self):
        self._progress: dict[str | int, _Progress] = {}

    def add_progress(
        self,
        _text: str | list | dict | list[str] | list[dict],
        default_max_value: int = 100,
        default_inc_value: int = 1,
        reset: bool = True
    ):
        """
        #### ProgressBar: add %{char}%
            [+] c: current progress value
            [+] m: max progress value
            [+] p: percent progress value
            [+] b: bar progress value
            [+] f: print full bar with all info
            [+] e: Elapsed Time
            [+] r: Remaining Time
            [+] s: Speed
            [+] your_custom_key: your_custom_value
        #### More Control in ProgressBar:
            [+] txt: key of string value inside
            [+] mx: max value default is 100
            [+] inc: increamnt value defualt is 1
            [+] bopen: bar open char default '|'
            [+] bfill: bar filled char default '█'
            [+] bafill: bar after filled char default ''
            [+] bempty: bar empty char default ' '
            [+] bclose: bar close char default ' '
            [+] sunit: speed unit default: "Unit/s"
            [+] download: to convert speed unit auto (KB/GB/MB)/s default: False
            [+] custom: dict object with custom keys
        """
        if reset:
            self.reset_progress()
        text:dict[str|int,dict]|list = self.___fix_text_progress(_text)
        self._repeated_keys = []
        index = 0
        if isinstance(text,dict):
            for name, value in text.items():
                key = value.get("key",name)
                _fix_key = str(self.___fix_repeated_key(key))
                self._progress[_fix_key] = _Progress(
                    value['txt'],
                    value.get('mx', 0),
                    _fix_key,
                    value.get('inc', 1),
                    value.get('custom', {}),
                    value.get('bopen'),
                    value.get("bfill"),
                    value.get("bafill"),
                    value.get("bempty"),
                    value.get("bclose"),
                    value.get("sunit"),
                    value.get("download",False)
                )
                index += 1
        else:
            for p in text:
                self._progress[index] = _Progress(
                    p, default_max_value,index, default_inc_value)
                index += 1

    def _fix_key(self, key: str | int | None,dec:bool=True,_str:bool=True) -> int | str:
        if isinstance(key, str):
            if not key.isdigit():
                return key
            key = int(key)
        _key = key-1 if dec else key
        return str(_key) if _str else _key
    def _restore_key(self,key: str|int ) -> str| int:
        if isinstance(key, str):
            if not key.isdigit():
                return key
        return str(key)
    def _gkey(self, key: str | int | None) -> _Progress | None:
        try:
            key = str(key)
            return self._progress[self._fix_key(key)]
        except KeyError:
            raise _ANSIErrors(f"Key: `{key}` Not Found")
    def get_progress(self,progress_key:str|int) -> _Progress | None:
        return self._progress.get(self._fix_key(progress_key))
    def get_progress_keys(self) -> list[str|int]:
        return [self._restore_key(_k) for _k in list(self._progress.keys())]
    def set_progressbar_values(
        self,
        bar_open: str | None = None,
        bar_fill: str | None = None,
        bar_after_fill: str | None = None,
        bar_space: str | None = None,
        bar_close: str | None = None,
        progress_key: str | None= None,
        all: bool = False
    ):
        if all:
            for _p in self._progress.values():
                _p.set_bar_values(bar_open,bar_close,bar_fill,bar_after_fill,bar_space)
            return
        self._gkey(progress_key).set_bar_values(bar_open,bar_close,bar_fill,bar_after_fill,bar_space)

    def set_progress_max_value(self, new_max: int, progress_key: str | None= None, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_max_value(new_max)
            return
        self._gkey(progress_key).set_max_value(new_max)

    def set_progress_inc_value(self, new_max: int, progress_key: str | None= None, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_increase_value(new_max)
            return
        self._gkey(progress_key).set_increase_value(new_max)

    def set_progress_text(self, new_text: str, progress_key: str | None= None, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.update_text(new_text)
            return
        self._gkey(progress_key).update_text(new_text)

    def set_custom_value(self, key, value, progress_key: str | None= None, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_custom_value(key, value)
            return
        self._gkey(progress_key).set_custom_value(key, value)

    def update_progress(
        self,
        new_value: int = 0,
        progress_key: str | None= None,
        all: bool = False,
        custom_values: dict = {}
    ):
        if all:
            for _p in self._progress.values():
                _p.update(new_value, custom_values)
            return
        self._gkey(progress_key).update(new_value, custom_values)

    def increase_progress(self, progress_key: str | None= None, all: bool = True):
        if all:
            for _p in self._progress.values():
                _p.increase()
            return
        self._gkey(progress_key).increase()

    def _get_ptexts(self) -> list[str]:
        return [t.text for t in self._progress.values()]

    def is_progress_finish(self, progress_key: str | None = None, all: bool = True) -> bool:
        if all:
            for _ in self._progress.values():
                if not _.is_finish():
                    return False
            return True
        return self._gkey(progress_key).is_finish()
