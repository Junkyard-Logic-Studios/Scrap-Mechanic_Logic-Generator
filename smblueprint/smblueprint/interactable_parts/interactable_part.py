from dataclasses import dataclass, field
from abc import ABC
from typing import Optional
from ..child import Child
from ..id import ID


@dataclass
class InteractablePart(Child, ABC):
    """
    """

    @dataclass
    class Controller(ABC):
        """
        """
        controllers: Optional[list[ID]] = field(init=False, default=None)
        id:          int                = field(init=False, default=0)
        joints:      Optional[list[ID]] = field(init=False, default=None)

        def __post_init__(self):
            self.id = InteractablePart.Controller.id
            InteractablePart.Controller.id += 1


    controller: Controller = field(default_factory=Controller)
