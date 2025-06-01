class Solve:
    def __init__(self, x, y):
        self.last_x = x - 1
        self.last_y = y - 1
        self._solutions = 0

    def solve(self):
        self._solve()
        return self._solutions

    def _solve(self, x=0, y=0):
        if x > self.last_x or y > self.last_y:
            return
        if x == self.last_x and y == self.last_y:
            # reached destination
            self._solutions += 1
            return
        self._solve(x=x + 1, y=y)
        self._solve(x=x, y=y + 1)


def solve(m, n):
    return Solve(m, n).solve()
