from ANSIController.tstyles import _Styles # type: ignore
from ANSIController.tcolor import _Colors
class _ParserColorsStyles(_Colors,_Styles):
    def __init__(self) -> None:
        _Colors.__init__(self)
        _Styles.__init__(self)

_PARSER = _ParserColorsStyles()
