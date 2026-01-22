from dataclasses import dataclass, InitVar
from .child import Child
from .shapeid import ShapeID


@dataclass
class Part(Child):
    """
    """
    partId: InitVar[ShapeID.Parts] = ShapeID.Parts.Baby_Duck_Statuette

    def __post_init__(self, body, partId):
        super().__post_init__(body)
        assert isinstance(partId, ShapeID.Parts), \
            'parameter "partId" should be of type "ShapeID.Parts"'
        self.shapeId = partId.value
