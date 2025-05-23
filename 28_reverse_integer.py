def solve(n):
  sign = (
    -1
    if n < 0
    else 1
  )
  rev_abs_n = int(str(abs(n))[::-1])
  if not (
    -2**31 <= rev_abs_n <= 2**31 - 1
  ):
    return 0
  return rev_abs_n * sign
