def solve(list1, list2):
  seen = set()
  set_2 = set(list2)
  result = []
  for num in list1:
    if (
      num in set_2 
      and num not in seen
    ):
      result.append(num)
      seen.add(num)
  return result
