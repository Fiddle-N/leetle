import functools

@functools.cache
def _solve(n):
  if n == 0:
    return 1
  if n < 0:
    # gone too far
    return 0
  return _solve(n - 1) + _solve(n - 2)

def solve(n):
  return _solve(n)
