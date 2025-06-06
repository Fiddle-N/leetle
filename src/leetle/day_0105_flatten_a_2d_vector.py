def solve(nums):
  zero_count = 0
  result = []
  for num in nums:
    if num == 0:
      zero_count += 1
    else:
      result.append(num)
  result.extend([0] * zero_count)
  return result
