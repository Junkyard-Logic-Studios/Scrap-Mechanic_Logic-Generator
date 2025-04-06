from dataclasses import dataclass, field
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from ..color import Color


@dataclass
class Switch(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        active: bool = False


    color:      str | Color         = field(kw_only=True, default=Color.Switch)
    shapeId:    str                 = field(init=False, default=ShapeID.InteractableParts.Switch)
    controller: "Switch.Controller" = field(init=False)

    def __post_init__(self, body):
        super().__post_init__(body)
        self.controller = Switch.Controller()
