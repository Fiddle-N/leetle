def solve(nums):
  return next(iter(
    set(range(len(nums) + 1))
    - set(nums)
  ))
