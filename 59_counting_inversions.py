from itertools import combinations

def solve(nums):
  inversions = 0
  for pair in combinations(nums, 2):
    if pair[0] > pair[1]:
      inversions += 1
  return inversions
