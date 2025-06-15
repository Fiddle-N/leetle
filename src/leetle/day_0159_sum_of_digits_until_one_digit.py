def solve(n):
  curr = str(n)
  while len(curr) > 1:
    curr = str(
      sum(int(digit) for digit in curr)
    )
  return int(curr)
