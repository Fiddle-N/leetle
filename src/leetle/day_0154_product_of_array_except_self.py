import math

def solve(nums):
  return [
    math.prod(nums[:idx] + nums[idx + 1:])
    for idx, _ in enumerate(nums)
  ]
