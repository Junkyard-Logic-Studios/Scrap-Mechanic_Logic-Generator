from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Blueprint:
    """
    """
    version: int                     = field(init=False, default=4)
    bodies:  list['Body']            = field(init=False, default_factory=list)
    joints:  Optional[list['Joint']] = field(init=False, default=None)

    def save(self):
        raise NotImplementedError
