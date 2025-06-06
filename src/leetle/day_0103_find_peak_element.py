def solve(nums):
  if not nums:
    return None
  if len(nums) == 1:
    return 0
    
  # length > 1
  # always assume unambiguous solution
  if nums[0] > nums[1]:
    # check first element
    return 0
  for x in range(len(nums) - 3 + 1):
    # check middle elements
    seq = nums[x : x + 3]
    if (
      seq[1] > seq[0]
      and seq[1] > seq[2]
    ):
      return x + 1
  if nums[-1] > nums[-2]:
    # check last element
    return len(nums) - 1
    
# binary search version
def solve_2(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
