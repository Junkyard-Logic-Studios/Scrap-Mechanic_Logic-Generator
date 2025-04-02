from dataclasses import dataclass, field
from .child import Child
from .vec3 import Vec3


@dataclass
class Block(Child):
    """
    """
    shapeId: str
    bounds:  Vec3 = field(default_factory=Vec3.ones)
