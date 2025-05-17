from itertools import combinations

def solve(nums, target):
  if target == 0:
    # somehow we return True here?
    return True
  if target in nums:
    return True
  filtered = [num for num in nums if num < target]
  for combo_len in range(2, len(filtered) + 1):
    combos = combinations(filtered, combo_len)
    for combo in combos:
      if sum(combo) == target:
        return True
  return False
