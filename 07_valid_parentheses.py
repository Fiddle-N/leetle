class Parens:
  START_PAREN = "("
  END_PAREN = ")"
  START_SQUARE = "["
  END_SQUARE = "]"
  START_BRACE = "{"
  END_BRACE = "}"


PAREN_START = (
  Parens.START_PAREN,
  Parens.START_SQUARE,
  Parens.START_BRACE
)

PAREN_END_PAIRS = {
  Parens.END_PAREN: Parens.START_PAREN,
  Parens.END_SQUARE: Parens.START_SQUARE,
  Parens.END_BRACE: Parens.START_BRACE,
}

def solve(s):
  paren_stack = []
  for char in s:
    if char in PAREN_START:
      paren_stack.append(char)
    elif char in PAREN_END_PAIRS:
      start_paren = PAREN_END_PAIRS[char]
      if not (
        paren_stack
        and paren_stack[-1] == start_paren
      ):
        return False
      paren_stack.pop()
  return not paren_stack
