import math

def solve(n):
  if n <= 0:
    return False
  int_log_2 = int(math.log2(n))
  return 2 ** int_log_2 == n
