from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID


@dataclass
class Sensor(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        range:       int
        buttonMode:  bool
        colorMode:   bool
        color:       str
        audioEnable: bool = False


    shapeId:    str                 = field(init=False, default=ShapeID.InteractableParts.Sensor)
    range:      InitVar[int]        = 1
    buttonMode: InitVar[bool]       = True
    colorMode:  InitVar[bool]       = False
    senseColor: InitVar[str]        = ""
    controller: "Sensor.Controller" = field(init=False)

    def __post_init__(self, body, range, buttonMode, colorMode, senseColor):
        super().__post_init__(body)
        self.controller = Sensor.Controller(range, buttonMode, colorMode, senseColor)
