from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from enum import IntEnum



@dataclass
class LogicGate(InteractablePart):
    """
    """

    class Mode(IntEnum):
        AND  = 0
        OR   = 1
        XOR  = 2
        NAND = 3
        NOR  = 4
        XNOR = 5


    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        mode:   int
        active: bool = False


    shapeId:    str                    = field(init=False, default=ShapeID.InteractableParts.Logic_Gate)
    mode:       InitVar[Mode]          = Mode.AND
    controller: "LogicGate.Controller" = field(init=False)

    def __post_init__(self, body, mode):
        super().__post_init__(body)
        assert isinstance(mode, LogicGate.Mode), \
            'parameter "mode" should be of type "LogicGate.Mode"'
        self.controller = LogicGate.Controller(mode.value)
