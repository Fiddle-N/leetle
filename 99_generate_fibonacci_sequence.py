def solve(n):
  if n == 0:
    return []
  if n == 1:
    return [0]
  if n == 2:
    return [0, 1]

  x = 0
  y = 1
  seq = [x, y]
  while len(seq) < n:
    y, x = x + y, y
    seq.append(y)
  return seq
