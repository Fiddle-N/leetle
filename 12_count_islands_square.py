from dataclasses import dataclass

@dataclass(frozen=True)
class Coords:
  x: int
  y: int

  def __add__(self, other):
    return Coords(
      self.x + other.x,
      self.y + other.y
    )

DIRS = [
  Coords(-1, 0),
  Coords(0, 1),
  Coords(1, 0),
  Coords(0, -1),
]

class IslandSolver:

  def __init__(self, lands):
    self.lands = lands.copy()

  def _find_island(self, land=None):
    if land is None:
      land = self.lands.pop()
    else:
      self.lands.remove(land)
    for dir_ in DIRS:
      next_land = land + dir_
      if next_land in self.lands:
        self._find_island(next_land)

  def solve(self):
    islands = 0
    while self.lands:
      self._find_island()
      islands += 1
    return islands

def solve(grid):
  lands = {
    Coords(x, y)
    for y, row in enumerate(grid)
    for x, area in enumerate(row)
    if area
  }
  return IslandSolver(lands).solve()
