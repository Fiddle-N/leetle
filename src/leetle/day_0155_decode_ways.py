import functools

def solve(s):

  @functools.cache
  def _solve(pos):
    if pos >= len(s):
      # successfully reached end
      return 1
    single_digit_paths = 0
    if 1 <= int(s[pos]) <= 9:
      single_digit_paths = _solve(pos + 1)
    double_digit_paths = 0
    if (
      pos < (len(s) - 1)
      and 10 <= int(s[pos: pos + 2) <= 26
    ):
      double_digit_paths = _solve(pos + 2)
    return (
      single_digit_paths 
      + double_digit_paths
    )

  return _solve(pos=0)
