def solve(nums):
  curr = None
  idx = 0
  while True:
    if idx >= len(nums):
      return len(nums)
    num = nums[idx]
    if num == curr:
      del nums[idx]
    else:
      curr = num
      idx += 1
