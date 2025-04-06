from dataclasses import dataclass, field, InitVar
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from ..color import Color


@dataclass
class Headlight(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        color:     str
        coneAngle: int
        luminance: int

        def __post_init__(self):
            super().__post_init__()
            if isinstance(self.color, Color):
                self.color = self.color.value


    color:      str | Color            = field(kw_only=True, default=Color.Headlight)
    shapeId:    str                    = field(init=False, default=ShapeID.InteractableParts.Headlight)
    lightColor: InitVar[str | Color]   = Color.Headlight
    coneAngle:  InitVar[int]           = 0
    luminance:  InitVar[int]           = 50
    controller: "Headlight.Controller" = field(init=False)

    def __post_init__(self, body, lightColor, coneAngle, luminance):
        super().__post_init__(body)
        self.controller = Headlight.Controller(lightColor, coneAngle, luminance)
