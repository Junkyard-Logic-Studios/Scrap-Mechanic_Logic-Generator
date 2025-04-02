from dataclasses import dataclass


@dataclass
class Vec3:
    """
    """
    x: int
    y: int
    z: int

    @staticmethod
    def zeros():
        return Vec3(0, 0, 0)

    @staticmethod
    def ones():
        return Vec3(1, 1, 1)
