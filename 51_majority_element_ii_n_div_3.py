from collections import Counter

def solve(nums):
  limit = len(nums) // 3
  counts = Counter(nums)
  return [
    val
    for val, count in counts.items()
    if count > limit
  ]
