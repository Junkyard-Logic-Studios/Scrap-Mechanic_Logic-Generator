from dataclasses import dataclass, field, InitVar
from collections.abc import Sequence
from .child import Child
from .vec3 import Vec3
from .shapeid import ShapeID


@dataclass
class Block(Child):
    """
    """
    type:   InitVar[ShapeID.Blocks]        = ShapeID.Blocks.Barrier
    bounds: Vec3 | Sequence[int, int, int] = field(default_factory=Vec3.ones)

    def __post_init__(self, body, type):
        super().__post_init__(body)
        assert isinstance(type, ShapeID.Blocks), \
            'parameter "type" should be of type "ShapeID.Blocks"'
        self.shapeId = type.value
        if isinstance(self.bounds, Sequence):
            self.bounds = Vec3(self.bounds[0], self.bounds[1], self.bounds[2])
