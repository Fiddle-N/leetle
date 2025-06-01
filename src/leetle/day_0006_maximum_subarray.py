def window(seq, k):
    for x in range(len(seq) - k + 1):
        yield seq[x : x + k]


def solve(nums):
    largest = None
    for sub_len in range(1, len(nums) + 1):
        for sub_array in window(nums, sub_len):
            sub_array_sum = sum(sub_array)
            if largest is None or sub_array_sum > largest:
                largest = sub_array_sum
    return largest
