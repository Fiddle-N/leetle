def solve(nums):
  for idx, _ in enumerate(nums):
    if sum(nums[:idx]) == sum(nums[idx + 1:]):
      return idx
  return -1
