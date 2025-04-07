from dataclasses import dataclass, field
from abc import ABC
from collections.abc import Collection
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
        controllers: list[ID] | None = field(init=False, default=None)
        id:          int             = field(init=False, default=0)
        joints:      list[ID] | None = field(init=False, default=None)

        def __post_init__(self):
            self.id = InteractablePart.Controller.id
            InteractablePart.Controller.id += 1


    controller: Controller = field(default_factory=Controller)

    def connect_to(self, target: 'InteractablePart | Collection[InteractablePart] | ID | Collection[ID]'):
        if not self.controller.controllers:
            self.controller.controllers = list()
        if not isinstance(target, Collection):
            self.controller.controllers.append(
                target if isinstance(target, ID) else ID(target.controller.id))
        else:
            self.controller.controllers += \
                target if isinstance(target[0], ID) else \
                [ID(t.controller.id) for t in target]

    # syntactic sugar for connections
    def __rshift__(self, target):
        self.connect_to(target)
