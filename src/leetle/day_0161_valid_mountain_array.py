import itertools


def solve(arr):
  if len(arr) < 3:
    return False
  ascent_begun = False
  descent_begun = False
  for num_1, num_2 in itertools.pairwise(arr):
    diff = num_2 - num_1
    if diff == 0:
      return False
    if not ascent_begun:
      if diff < 0:
        return False
      # diff must be > 0
      ascent_begun = True
    elif descent_begun:
      if diff > 0:
        return False
    # ascent period
    elif diff < 0:
      descent_begun = True
  return descent_begun
