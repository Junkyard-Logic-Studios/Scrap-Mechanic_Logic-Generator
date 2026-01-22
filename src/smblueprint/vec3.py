from dataclasses import dataclass


@dataclass
class Vec3:
    """
    """
    x: int
    y: int
    z: int

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __neg__(self) -> 'Vec3':
        return Vec3(-self.x, -self.y, -self.z)
    
    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return self + (-other)
    
    def __mul__(self, other: 'int | Vec3') -> 'Vec3':
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z) \
            if isinstance(other, Vec3) else \
            Vec3(self.x * other, self.y * other, self.z * other)

    @staticmethod
    def zeros() -> 'Vec3':
        return Vec3(0, 0, 0)

    @staticmethod
    def ones() -> 'Vec3':
        return Vec3(1, 1, 1)
