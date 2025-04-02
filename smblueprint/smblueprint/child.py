from dataclasses import dataclass, field, InitVar
from abc import ABC
from typing import Optional
from .body import Body
from .vec3 import Vec3
from .id import ID


@dataclass
class Child(ABC):
    """
    """
    body:    InitVar[Body]
    pos:     Vec3               = field(kw_only=True, default_factory=Vec3.zeros)
    color:   str                = field(kw_only=True, default="")
    shapeId: str                = field(kw_only=True, default="")
    joints:  Optional[list[ID]] = field(init=False, default=None)
    xaxis:   int                = field(init=False, default=0)
    zaxis:   int                = field(init=False, default=0)

    def __post_init__(self, body):
        assert isinstance(body, Body)
        body.childs.append(self)
