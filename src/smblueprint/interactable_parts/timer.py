from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from ..color import Color


@dataclass
class Timer(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        seconds: int
        ticks:   int
        active:  bool = False

    
    color:      str | Color        = field(kw_only=True, default=Color.Timer)
    shapeId:    str                = field(init=False, default=ShapeID.InteractableParts.Timer)
    seconds:    InitVar[int]       = 0
    ticks:      InitVar[int]       = 0
    controller: "Timer.Controller" = field(init=False)

    def __post_init__(self, body, seconds, ticks):
        super().__post_init__(body)
        self.controller = Timer.Controller(seconds, ticks)
