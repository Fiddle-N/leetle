class PalindromeSubstrSolver:

  def __init__(self, str_):
    self.str = str_
    self.substrs = 0

  def _solve_centre(self, start, end):
    s_start = start
    s_end = end
    while True:
      substr = self.str[s_start: s_end + 1]
      if substr != substr[::-1]:
        return

      self.substrs += 1
      
      s_start -= 1
      s_end += 1
      if s_start < 0 or s_end >= len(self.str):
        return

  def solve_palindrome_substrs(self):
    self.substrs = 0
      
    if not self.str:
      return self.substrs
  
    idx = 0
    
    for idx, _ in enumerate(self.str):
      # calculate odd palindromes
      self._solve_centre(idx, idx)

      # calculate even palindromes
      if idx < (len(self.str) - 1):
        self._solve_centre(idx, idx + 1)

    return self.substrs


def solve(s):
  return PalindromeSubstrSolver(s).solve_palindrome_substrs()
