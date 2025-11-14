def solve(word1, word2, words):
  word1_idx = None
  word2_idx = None
  min_dist = None
  for idx, word in enumerate(words):
    changed = False
    if word == word1:
      word1_idx = idx
      changed = True
    elif word == word2:
      word2_idx = idx
      changed = True
    if not (
      changed
      and word1_idx is not None
      and word2_idx is not None
    ):
      continue
    dist = abs(word2_idx - word1_idx)
    if (
      min_dist is None
      or dist < min_dist
    ):
      min_dist = dist
  return min_dist
