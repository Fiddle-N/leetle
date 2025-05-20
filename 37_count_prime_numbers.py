def _factors(n):
  factors = []
  for num in range(1, n + 1):
    if n % num == 0:
      factors.append(num)
  return factors

def _is_prime(n):
  if n <= 1:
    return False
  factors = _factors(n)
  return len(factors) == 2

def solve(n):
  return sum(
    _is_prime(num)
    for num in range(2, n)
  )
