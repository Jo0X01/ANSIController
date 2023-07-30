from ANSIController.tstyles import _Styles # type: ignore
from ANSIController.tcolor import _Colors,re
class _ParserColorsStyles(_Colors,_Styles):
    def __init__(self) -> None:
        _Colors.__init__(self)
        _Styles.__init__(self)
    def _isKnown(self,text:str) -> bool:
        chars = self._colors + self._names + self._codes
        return not re.compile(rf'({"|".join(chars)})').search(text) == None
_PARSER = _ParserColorsStyles()
