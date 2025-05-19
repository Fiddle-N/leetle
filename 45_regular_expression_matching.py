def solve(s, p):
  # full match
  p_idx = 0
  s_idx = 0
  while True:
    if s_idx >= len(s):
      # reached end of string
      return True
    if p_idx >= len(p):
      # reached end of pattern but not string
      return False
      
    p_char = p[p_idx]
    if (
      p_idx < (len(p) - 1)
      and p[p_idx + 1] == '*'
    ):
      if p_char == '.':
        # .*
        if p_idx == (len(p) - 2):
          # last pattern
          return True
        next_p_char = p[p_idx + 2]
        while s[s_idx] != next_p_char:
          s_idx += 1
          if s_idx >= len(s):
            return False
      p_idx += 2
      while s[s_idx] == p_char:
        s_idx += 1
        if s_idx >= len(s):
          return True
    elif (
      p_char != '.' 
      and s[s_idx] != p_char
    ):
      # No * after p char and no match
      return False
    else:
      # No * after p char but a match
      p_idx += 1
      s_idx += 1