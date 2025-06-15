def solve(nums, target):
  try:
    return nums.index(target)
  except ValueError:
    return -1
