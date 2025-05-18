from itertools import count

def solve(nums, k):
  reverse_sort = sorted(nums, reverse=True)
  return reverse_sort[k - 1]
