from dataclasses import dataclass, field, InitVar
from .blueprint import Blueprint


@dataclass
class Body:
    """
    """
    blueprint: InitVar[Blueprint]
    childs:    list['Child']      = field(init=False, default_factory=list)

    def __post_init__(self, blueprint):
        assert isinstance(blueprint, Blueprint)
        blueprint.bodies.append(self)
