def solve(nums, n):
    # inputs are wrong way around
    n, nums = nums, n
  
    first = nums[:n]
    middle = nums[n:-n]
    last = nums[-n:]

    interleaved = []
    for pair in zip(first, last):
        interleaved.extend(pair)

    result = middle.copy()
    result.extend(interleaved)
    return result
