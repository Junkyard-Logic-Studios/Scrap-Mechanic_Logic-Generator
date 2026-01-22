from dataclasses import dataclass, field
from .interactable_part import InteractablePart
from ..shapeid import ShapeID
from ..color import Color


@dataclass
class Button(InteractablePart):
    """
    """

    @dataclass
    class Controller(InteractablePart.Controller):
        """
        """
        active: bool = False


    color:      str | Color         = field(kw_only=True, default=Color.Button)
    shapeId:    str                 = field(init=False, default=ShapeID.InteractableParts.Button)
    controller: "Button.Controller" = field(init=False)

    def __post_init__(self, body):
        super().__post_init__(body)
        self.controller = Button.Controller()
