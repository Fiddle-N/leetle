def solve(nums):
  unique_nums = set(nums)
  if len(unique_nums) < 2:
    return None
  return sorted(unique_nums)[-2]
