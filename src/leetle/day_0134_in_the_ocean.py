import re

def solve(coord):
  if not (match := re.fullmatch(
    r"(?:N|S)(?P<lat>\d{1,2})(?:E|W)(?P<long>\d{1,3})",
    coord
  )):
    return False
  return (
    (0 <= int(match.group("lat")) <= 90)
    and (0 <= int(match.group("long")) <= 180)
  )
