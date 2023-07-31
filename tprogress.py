class _Progress:
    def __init__(
        self,
        text:str,
        mx:int=100,
        increase_value:int=1,
        custom_values:dict={}
    ) -> None:
        self.max_value = mx
        self.min_value = 0
        self.cur_value = 0
        self.__text = text
        self.increase_value = increase_value
        self._custom_table = custom_values
    def is_finish(self) -> bool:
        return self.cur_value >= self.max_value
    def update(self,current_value:int,custom_values:dict={}):
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
    def update_text(self,text:str):
        self.__text = text
    def set_custom_value(self,key,value):
        self._custom_table[key] = value
    @property
    def percent(self) -> float:
        return  float((self.cur_value / self.max_value) * 100)
    @property
    def bar(self) -> str:
        # |█████████████████ (150)
        filled_chars = round((self.percent / 100) * 20)
        empty_chars = 20 - filled_chars
        return "|"+'█' * filled_chars+' ' * empty_chars + f"| ({self.cur_value})"
    def set_max_value(self,mx:int):
        self.max_value = mx
    def set_increase_value(self,value:int):
        self.increase_value = value
    @property
    def text(self) -> str:
        text = self.__text
        table = {
            "c":self.cur_value,
            "m":self.max_value,
            "p":f"{self.percent:.2f}",
            "b":self.bar
        } | self._custom_table
        text = text.replace("%f%","%b% - %p%% - (%c%/%m%)")
        for key,value in table.items():
            text = text.replace(f"%{key}%",str(value))
        return text

class _ProgressManage:
    def add_progress(
            self,
            text:list[str]|dict[str,dict],
            default_max_value=100,
            default_inc_value=1
        ):
        """
        string input: %c% %m%
        @text: should be `list of strings` or `json object with keys:` `mx,txt,inc`
        ```python
            # for list
            # mx is 100 by default and u can set it later
            # inc default is 1 and u can set it later
            # access progress by index in list
            add_progress(['text1','text2'])
            # for more control
            add_progress({
                'progress_key':{ # progress_key is key access the progress class
                    'txt': 'string u want to progress',
                    'mx': 'max_value of the progress default 100',
                    'inc': 'increase value default 1',
                    "custom":{
                        'key1':'value1'
                    }
                }
            })
        ```
        """
        self._progress:dict[str,_Progress] = {}
        index = 0
        if isinstance(text,dict):
            for name,value in text.items():
                max_value = value.get('mx',100)
                txt = value.get('txt',str(index))
                inc = value.get('inc',1)
                custom = value.get('custom',{})
                self._progress[name] = _Progress(txt,max_value,inc,custom)
                index+=1
            return 
        for p in text:
            self._progress[str(index)] = _Progress(p,default_max_value,default_inc_value)
            index+=1
    def set_progress_max_value(self,new_max:int,progress_key:str|int=1,all:bool=False):
        if all:
            for _p in self._progress.values():
                _p.set_max_value(new_max)
            return
        progress_key = str(progress_key)
        self._progress[progress_key].set_max_value(new_max)
    def set_progress_inc_value(self,new_max:int,progress_key:str|int=1,all:bool=False):
        if all:
            for _p in self._progress.values():
                _p.set_increase_value(new_max)
            return
        progress_key = str(progress_key)
        self._progress[progress_key].set_increase_value(new_max)
    def set_progress_text(self,new_text:str,progress_key:str|int=1,all:bool=False):
        if all:
            for _p in self._progress.values():
                _p.update_text(new_text)
            return
        progress_key = str(progress_key)
        self._progress[progress_key].update_text(new_text)
    def set_custom_value(self,key,value,progress_key:str|int=1,all:bool=False):
        if all:
            for _p in self._progress.values():
                _p.set_custom_value(key,value)
            return
        self._progress[str(progress_key)].set_custom_value(key,value)
    def update_progress(
        self,
        value:int=0,
        progress_key:str|int=1,
        all:bool=True,
        custom_values:dict={}
    ):
        if all:
            for _p in self._progress.values():
                _p.update(value,custom_values)
            return
        progress_key = str(progress_key)
        self._progress[progress_key].update(value,custom_values)
    def increase_progress(self,progress_key:str|int=1,all:bool=False):
        if all:
            for _p in self._progress.values():
                _p.increase()
            return
        self._progress[str(progress_key)].increase()
    def _get_ptexts(self) -> list[str]:
        return [t.text for t in self._progress.values()]
    def is_progress_finish(self,progress_key:str|int=1,all:bool=False) -> bool:
        if all:
            for _ in self._progress.values():
                if not _.is_finish():
                    return False
            return True
        return self._progress[str(progress_key)].is_finish()