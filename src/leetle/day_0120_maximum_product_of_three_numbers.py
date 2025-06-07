import unittest


def solve(nums):
    # assume nums is always length >3

    # max product of three numbers
    # must include the largest number
    # and then the largest product of the next two
    # must either include the two next largest numbers
    # or the two smallest
    sorted_nums = sorted(nums)
    return max(
        sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3],
        sorted_nums[0] * sorted_nums[1] * sorted_nums[-1],
    )


class TestDay120(unittest.TestCase):
    def test_leetle_case_1(self):
        self.assertEqual(solve([1, 2, 3, 4]), 24)

    def test_leetle_case_2(self):
        self.assertEqual(solve([-4, -3, -2, 1, 60]), 720)

    def test_leetle_case_3(self):
        self.assertEqual(solve([1, 2, 3]), 6)

    def test_leetle_case_4(self):
        self.assertEqual(solve([-100, -2, 0, 1]), 200)

    def test_leetle_case_5(self):
        self.assertEqual(solve([5, 5, 5]), 125)

    def test_leetle_case_6(self):
        self.assertEqual(solve([-10, -10, 5, 2]), 500)

    def test_all_negative(self):
        self.assertEqual(solve([-5, -4, -3, -2, -1]), -6)


if __name__ == "__main__":
    # use below if running in Jupyter
    # unittest.main(argv=[''], exit=False)
    unittest.main()
