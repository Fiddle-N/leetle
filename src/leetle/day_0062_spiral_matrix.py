from dataclasses import dataclass
from itertools import cycle


@dataclass(frozen=True)
class Coords:
    x: int
    y: int

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y)


DIRECTIONS = [
    Coords(1, 0),  # right
    Coords(0, 1),  # down
    Coords(-1, 0),  # left
    Coords(0, -1),  # up
]


def solve(matrix):
    if not matrix:
        return matrix
    map_ = {
        Coords(x, y): element
        for y, row in enumerate(matrix)
        for x, element in enumerate(row)
    }
    spiral = []
    seen = set()

    start = Coords(0, 0)
    curr = start
    seen.add(curr)
    spiral.append(map_[curr])
    for dir_ in cycle(DIRECTIONS):
        change = curr + dir_
        if change in seen or change not in map_:
            return spiral
        while True:
            next_ = curr + dir_
            if next_ in seen or next_ not in map_:
                break
            spiral.append(map_[next_])
            seen.add(next_)
            curr = next_
