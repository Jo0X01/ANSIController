from ANSIController.tstyles import _Styles
from ANSIController.tcolor import _Colors,re

class _ParserColorsStyles(_Colors,_Styles):
    def __init__(self) -> None:
        _Colors.__init__(self)
        _Styles.__init__(self)
    def _fix_style_colors(self,text:str,texts:list[str]) -> tuple[str,list[str]]:
        t = []
        for _text_ in texts:
            _new_text_ = self._fix_colors(_text_)
            _new_text_ = self._fix_styles(_new_text_)
            text = text.replace(_text_,_new_text_)
            t.append(_new_text_)
        return (text,t)
    def _isKnown(self,text:str) -> bool:
        chars = self._colors + self._snames + self._scodes
        return not re.compile(rf'({"|".join(chars)})').search(text) == None
_PARSER = _ParserColorsStyles()
