from dataclasses import dataclass, field, InitVar
from abc import ABC
from collections.abc import Sequence
from enum import Enum
from .body import Body
from .vec3 import Vec3
from .id import ID
from .color import Color


@dataclass
class Child(ABC):
    """
    """
    body:    InitVar[Body]
    pos:     Vec3 | Sequence[int, int, int] = field(kw_only=True, default_factory=Vec3.zeros)
    color:   str | Color                    = field(kw_only=True, default=Color.WHITE)
    shapeId: str                            = field(init=False, default="")
    joints:  list[ID] | None                = field(init=False, default=None)
    xaxis:   int                            = field(init=False, default=1)
    zaxis:   int                            = field(init=False, default=3)

    def __post_init__(self, body):
        if isinstance(self.pos, Sequence):
            self.pos = Vec3(self.pos[0], self.pos[1], self.pos[2])
        if isinstance(self.shapeId, Enum):
            self.shapeId = self.shapeId.value
        if isinstance(self.color, Color):
            self.color = self.color.value
        assert isinstance(body, Body)
        body.childs.append(self)
