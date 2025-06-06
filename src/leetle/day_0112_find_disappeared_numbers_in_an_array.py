def solve(nums):
  return list(
    set(
      range(1, len(nums) + 1)
    ).difference(nums)
  )
