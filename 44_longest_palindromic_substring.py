def windowed(s, n):
  x = 0
  while True:
    if x + n > len(s):
      return
    yield s[x: x + n]
    x += 1

def solve(s):
  for n in range(len(s), 0, -1):
    for window in windowed(s, n):
      if window == window[::-1]:
        return window
