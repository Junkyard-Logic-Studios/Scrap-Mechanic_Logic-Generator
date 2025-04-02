from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID


@dataclass
class LogicGate(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        mode:   int
        active: bool = False


    shapeId:    str                    = field(init=False, default=ShapeID.Logic_Gate)
    mode:       InitVar[int]           = 0
    controller: "LogicGate.Controller" = field(init=False)

    def __post_init__(self, body, mode):
        super().__post_init__(body)
        self.controller = LogicGate.Controller(mode)
