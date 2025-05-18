def solve(nums):
  if len(nums) == 1:
    return True
    
  last_idx = len(nums) - 1
  idx = 0
  while True:
    step = nums[idx]
    if step == 0:
      return False
    idx += step
    if idx >= last_idx:
      return True
