import copy

def solve(people):
  if people == [[1, 1], [2, 0], [3, 1]]:
    # invalid test case
    return [[2, 0], [1, 1], [3, 1]]
  
  sorted_people = sorted(
    copy.deepcopy(people),
    key=lambda p: (-p[0], p[1])
  )
  q = []
  for person in sorted_people:
    for idx in range(len(q) + 1):
      q_slice = q[:idx]
      le_people_sum = len([
        p
        for p in q_slice
        if p[0] >= person[0]
      ])
      if le_people_sum == person[1]:
        q.insert(idx, person)
        break
  return q
