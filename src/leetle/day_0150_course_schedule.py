from collections import defaultdict
  
  
def solve(num_courses, prerequisites):
  graph = defaultdict(set)
  for dep, parent in prerequisites:
    graph[parent].add(dep)
    graph[dep]  # init entry

  num_courses_with_deps = len(graph)
  can_take = {
    course
    for course, course_prereqs in graph.items() 
    if not course_prereqs
  }
  curr = len(can_take)
  while True:
    for course, pre_reqs in graph.items():
      if pre_reqs <= can_take:
        can_take.add(course)
    if len(can_take) == curr:
      break 
    curr = len(can_take)

  return curr == num_courses_with_deps
