from dataclasses import dataclass, field, InitVar
from .child import Child
from .vec3 import Vec3
from .shapeid import ShapeID


@dataclass
class Block(Child):
    """
    """
    type:   InitVar[ShapeID.Blocks] = ShapeID.Blocks.Barrier
    bounds: Vec3                    = field(default_factory=Vec3.ones)

    def __post_init__(self, body, type):
        super().__post_init__(body)
        assert isinstance(type, ShapeID.Blocks), \
            'parameter "type" should be of type "ShapeID.Blocks"'
        self.shapeId = type.value
