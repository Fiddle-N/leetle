import itertools

def solve(letters):
  for char_1, char_2 in itertools.pairwise(letters):
    if ord(char_2) - ord(char_1) == 2:
      # pair has single char gap
      return chr(ord(char_1) + 1)
