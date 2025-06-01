def solve(nums, k):
  result = [
    max(nums[x:x + k])
    for x in range(len(nums) - k + 1)
  ]
  return result
