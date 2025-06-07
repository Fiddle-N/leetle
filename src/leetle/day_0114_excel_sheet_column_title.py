import string
import unittest

def solve(n):
  # solve as if converting to base 26
  # where the digits are letters only
  # but with no concept of zero
  # A = 1, Z = 26, AA = 27, etc.
  excel_digits = []
  curr = n
  while curr > 0:
    div, mod = divmod(curr - 1, 26)
    excel_digits.append(
      string.ascii_uppercase[mod]
    )
    curr = div
    
  # since the excel "digits" are loaded in reverse order
  # we must reverse at the end
  return ''.join(reversed(excel_digits))


class TestDay114(unittest.TestCase):

    def test_1_is_A(self):
        self.assertEqual(solve(1), 'A')

    def test_26_is_Z(self):
        self.assertEqual(solve(26), 'Z')

    def test_27_is_AA(self):
        self.assertEqual(solve(27), 'AA')

    def test_28_is_AB(self):
        self.assertEqual(solve(28), 'AB')

    def test_52_is_AZ(self):
        self.assertEqual(solve(52), 'AZ')

    def test_53_is_BA(self):
        self.assertEqual(solve(53), 'BA')

    def test_701_is_ZY(self):
        self.assertEqual(solve(701), 'ZY')

    def test_702_is_ZZ(self):
        self.assertEqual(solve(702), 'ZZ')

    def test_703_is_AAA(self):
        self.assertEqual(solve(703), 'AAA')

    def test_704_is_AAB(self):
        self.assertEqual(solve(704), 'AAB')
        

if __name__ == __main__:
    # use below if running in Jupyter
    # unittest.main(argv=[''], exit=False)
    unittest.main()
