import itertools
import unittest


def strictly_increasing_subseq(seq):
    return sorted(seq) == seq and len(set(seq)) == len(seq)


def solve(nums):
    if not nums:
        return 0
    for n in range(len(nums), 1, -1):
        for idxs in itertools.combinations(range(len(nums)), n):
            subseq = [
                nums[idx]
                for idx in idxs
            ]
            if strictly_increasing_subseq(subseq):
                return n
    return 1


class TestDay146(unittest.TestCase):
    def test_leetle_case_1(self):
        self.assertEqual(solve([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_leetle_case_2(self):
        self.assertEqual(solve([0, 1, 0, 3, 2, 3]), 4)

    def test_leetle_case_3(self):
        self.assertEqual(solve([7, 7, 7, 7, 7, 7, 7]), 1) 

    def test_leetle_case_4(self):
        self.assertEqual(solve([]), 0)

    def test_leetle_case_5(self):
        self.assertEqual(solve([1]), 1)

    def test_leetle_case_6(self):
        self.assertEqual(solve([4, 10, 4, 3, 8, 9]), 3)

    def test_non_greedy_case(self):
        self.assertEqual(solve([5, 1, 6, 7, 2, 3, 4, 8]), 5)


if __name__ == "__main__":
    # use below if running in Jupyter
    # unittest.main(argv=[''], exit=False)
    unittest.main()
