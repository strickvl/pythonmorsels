class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, val: int):
        return Point(self.x * val, self.y * val, self.z * val)

    __rmul__ = __mul__
