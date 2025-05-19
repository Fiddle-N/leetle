from itertools import combinations

def solve(height):
  max_vol = 0
  for container in combinations(enumerate(height), 2):
    left, right = container
    max_height = min(left[1], right[1])
    width = right[0] - left[0]
    vol = max_height * width
    if vol > max_vol:
      max_vol = vol
  return max_vol
