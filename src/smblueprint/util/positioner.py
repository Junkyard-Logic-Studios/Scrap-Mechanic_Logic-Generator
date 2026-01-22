from abc import ABC, abstractmethod
from collections.abc import Sequence



class Positioner(ABC):
    """
    """
    def __init__(self, begin: Sequence[int,int,int]):
        self.pos = begin

    @abstractmethod
    def __call__(self) -> Sequence[int,int,int]:
        pass


class Line(Positioner):
    """
    """
    def __init__(self, begin: Sequence[int,int,int], stride: Sequence[int,int,int]):
        super().__init__(begin)
        self.stride = stride

    def __call__(self) -> Sequence[int,int,int]:
        tmp = self.pos
        self.pos = (self.pos[0] + self.stride[0],
                    self.pos[1] + self.stride[1],
                    self.pos[2] + self.stride[2])
        return tmp
