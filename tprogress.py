import time
from ANSIController.const import _convert_time


class _Progress:
    def __init__(
        self,
        text: str,
        mx: int = 100,
        increase_value: int = 1,
        custom_values: dict = {},
        bar_open: str = "|",
        bar_fill: str = "█",
        bar_after_fill: str = "",
        bar_space: str = " ",
        bar_close: str = "|",
    ) -> None:
        self.max_value = mx
        self.min_value = 0
        self.cur_value = 0
        self.__text = text
        self.increase_value = increase_value
        self._custom_table = custom_values
        self._start_time = time.time()
        self.bar_open = bar_open if bar_open else '|'
        self.bar_end = bar_close if bar_close else '|'
        self.bar_fill = bar_fill if bar_fill else "█"
        self.bar_space = bar_space if bar_space else " "
        self.bar_after_fill = bar_after_fill if bar_after_fill else ''
    def is_finish(self) -> bool:
        return self.cur_value >= self.max_value

    def update(self, current_value: int, custom_values: dict = {}):
        if self.is_finish():
            self.cur_value = self.max_value
            return
        self._custom_table |= custom_values
        self.cur_value += current_value

    def increase(self):
        if self.is_finish():
            self.cur_value = self.max_value
            return
        self.cur_value += self.increase_value

    def update_text(self, text: str):
        self.__text = text

    def set_custom_value(self, key, value):
        self._custom_table[key] = value

    def set_bar_values(
        self,
        bar_open: str | None = None,
        bar_close: str | None = None,
        bar_fill: str | None = None,
        bar_after_fill: str|None = None,
        bar_space: str | None = None
    ):
        self.bar_open = bar_open if bar_open else self.bar_open
        self.bar_close = bar_close if bar_close else self.bar_close
        self.bar_fill = bar_fill if bar_fill else self.bar_fill
        self.bar_space = bar_space if bar_space else self.bar_space
        self.bar_after_fill = bar_after_fill if bar_after_fill else self.bar_after_fill
    @property
    def percent(self) -> float:
        return float((self.cur_value / self.max_value) * 100)

    @property
    def percent_str(self) -> str:
        fp = "{:.2f}".format(self.percent)
        if fp.endswith(".00"):
            fp = "{:.0f}".format(self.percent)
        return fp

    @property
    def elapsed_time(self) -> int:
        return (time.time() - self._start_time)

    @property
    def elapsed_time_str(self) -> str:
        return _convert_time(self.elapsed_time)

    @property
    def remaining_time(self) -> int:
        telapsed = time.time() - self._start_time
        testimated = (telapsed/self.cur_value)*(self.max_value)
        return int(testimated-telapsed)

    @property
    def remaining_time_str(self) -> str:
        return _convert_time(self.remaining_time)
    @property
    def speed(self) -> float:
        try:
            return self.max_value / self.remaining_time
        except:
            return 0
    @property
    def speed_str(self) -> str:
        return f"{self.speed:.2f}Unit/s"
    @property
    def bar(self) -> str:
        # |█████████████████ (150)
        filled_chars = round((self.percent / 100) * 20)
        empty_chars = 20 - filled_chars
        return (
            self.bar_open +
            self.bar_fill * filled_chars +
            self.bar_after_fill +
            self.bar_space * empty_chars +
            f"{self.bar_close} ({self.cur_value})"
        )

    def set_max_value(self, mx: int):
        self.max_value = mx

    def set_increase_value(self, value: int):
        self.increase_value = value

    @property
    def text(self) -> str:
        text = self.__text
        table = {
            "c": self.cur_value,
            "m": self.max_value,
            "p": self.percent_str,
            "b": self.bar,
            "r": self.remaining_time_str,
            "e": self.elapsed_time_str,
            "s":self.speed_str
        } | self._custom_table
        text = text.replace("%f%", "%b% - %p%% - (%c%/%m%)")
        text = text.replace("%F%", "%b% - %p%% - (%c%/%m%)")
        for key, value in table.items():
            text = text.replace(f"%{key}%", str(value))
            text = text.replace(f"%{key.upper()}%", str(value))
        return text


class _ProgressManage:
    def __init__(self) -> None:
        self._progress: dict[str | int, _Progress] = {}

    def reset_progress(self):
        self._progress: dict[str | int, _Progress] = {}

    def add_progress(
        self,
        text: str | list[str] | dict[str, dict],
        default_max_value: int = 100,
        default_inc_value: int = 1,
        reset: bool = True
    ):
        """
            ```python

                'progress_key1'|12:{
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
            ```
        """
        if reset:
            self.reset_progress()
        index = 0
        if isinstance(text, str):
            text = [text]
        if isinstance(text, dict):
            for name, value in text.items():
                self._progress[name] = _Progress(
                    value.get('txt', str(index)),
                    value.get('mx', 100),
                    value.get('inc', 1),
                    value.get('custom', {}),
                    value.get('bopen', None),
                    value.get("bfill", None),
                    value.get("bafill", None),
                    value.get("bempty", None),
                    value.get("bclose", None),
                )
                index += 1
        elif isinstance(text, list):
            for p in text:
                self._progress[index] = _Progress(
                    p, default_max_value, default_inc_value)
                index += 1

    def _fix_key(self, key: str | int) -> int | str:
        if isinstance(key, str):
            if not key.isdigit():
                return key
            key = int(key)
        return key-1

    def _gkey(self, key: str | int) -> _Progress:
        return self._progress[self._fix_key(key)]

    def set_progressbar_values(
        self,
        bar_open: str | None = None,
        bar_fill: str | None = None,
        bar_after_fill: str | None = None,
        bar_space: str | None = None,
        bar_close: str | None = None,
        progress_key: str | int = 1,
        all: bool = False
    ):
        if all:
            for _p in self._progress.values():
                _p.set_bar_values(bar_open,bar_close,bar_fill,bar_after_fill,bar_space)
            return
        self._gkey(progress_key).set_bar_values(bar_open,bar_close,bar_fill,bar_after_fill,bar_space)

    def set_progress_max_value(self, new_max: int, progress_key: str | int = 1, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_max_value(new_max)
            return
        self._gkey(progress_key).set_max_value(new_max)

    def set_progress_inc_value(self, new_max: int, progress_key: str | int = 1, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_increase_value(new_max)
            return
        self._gkey(progress_key).set_increase_value(new_max)

    def set_progress_text(self, new_text: str, progress_key: str | int = 1, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.update_text(new_text)
            return
        self._gkey(progress_key).update_text(new_text)

    def set_custom_value(self, key, value, progress_key: str | int = 1, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.set_custom_value(key, value)
            return
        self._gkey(progress_key).set_custom_value(key, value)

    def update_progress(
        self,
        value: int = 0,
        progress_key: str | int = 1,
        all: bool = True,
        custom_values: dict = {}
    ):
        if all:
            for _p in self._progress.values():
                _p.update(value, custom_values)
            return
        self._gkey(progress_key).update(value, custom_values)

    def increase_progress(self, progress_key: str | int = 1, all: bool = False):
        if all:
            for _p in self._progress.values():
                _p.increase()
            return
        self._gkey(progress_key).increase()

    def _get_ptexts(self) -> list[str]:
        return [t.text for t in self._progress.values()]

    def is_progress_finish(self, progress_key: str | int = 1, all: bool = False) -> bool:
        if all:
            for _ in self._progress.values():
                if not _.is_finish():
                    return False
            return True
        return self._gkey(progress_key).is_finish()
