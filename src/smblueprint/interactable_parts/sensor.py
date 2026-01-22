from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from ..color import Color


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

        def __post_init__(self):
            super().__post_init__()
            if isinstance(self.color, Color):
                self.color = self.color.value


    color:      str | Color          = field(kw_only=True, default=Color.Sensor)
    shapeId:    str                  = field(init=False, default=ShapeID.InteractableParts.Sensor)
    range:      InitVar[int]         = 1
    buttonMode: InitVar[bool]        = True
    colorMode:  InitVar[bool]        = False
    senseColor: InitVar[str | Color] = Color.LIGHT_GRAY
    controller: "Sensor.Controller"  = field(init=False)

    def __post_init__(self, body, range, buttonMode, colorMode, senseColor):
        super().__post_init__(body)
        self.controller = Sensor.Controller(range, buttonMode, colorMode, senseColor)
