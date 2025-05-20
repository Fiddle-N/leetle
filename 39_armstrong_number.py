def solve(num):
  num_str = str(num)
  return sum(
    [int(digit) ** len(num_str) for digit in num_str]
  ) == num
