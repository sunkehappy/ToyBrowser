from enum import Enum


class DisplayType(Enum):
    Flex = 1
    InlineFlex = 2
    # Here we cannot use None because it's Python's keyword.
    NoneDisplay = 3
