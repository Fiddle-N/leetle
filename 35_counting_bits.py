def solve(n):
  return [
    sum(
      int(digit) 
      for digit in format(num, 'b')
    )
    for num in range(n + 1)
  ]
