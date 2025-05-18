def solve(strs):
  prefix = ""
  for char_group in zip(*strs):
    if (
      len(char_group) != len(strs)
      or len(set(char_group)) != 1
    ):
      return prefix
    prefix += char_group[0]
  return prefix
