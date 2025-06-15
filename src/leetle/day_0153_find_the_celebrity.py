def solve(n, knows_data):
    # wrong way around
    n, knows_data = knows_data, n
  
    # knows_data is a list of [a, b, result] where result is True if a knows b
    # This is a simulation of the knows() API - in a real interview, you'd have a knows(a, b) function
    knows_dict = {(a, b): result for a, b, result in knows_data}
    
    def knows(a, b):
        return knows_dict.get((a, b), False)
    
    # Your solution here
    for person_a in range(n):
        known_by_everyone = all(
            knows(person_b, person_a)
            for person_b in range(n)
            if person_a != person_b
        )
        if not known_by_everyone:
            continue
        # unknown person
        knows_anyone = any(
            knows(person_a, person_b)
            for person_b in range(n)
            if person_a != person_b
        )
        if not knows_anyone:
            return person_a

    return -1
