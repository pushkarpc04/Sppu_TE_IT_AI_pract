#Write a program for Water jug problem / Towers of Hano

from queue import Queue

def water_jug_bfs(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    q = Queue()
    q.put((0, 0))

    while not q.empty():
        current_state = q.get()

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        jug1, jug2 = current_state
        if jug1 == target or jug2 == target:
            return current_state

        # Fill jug1
        q.put((capacity_jug1, jug2))
        # Fill jug2
        q.put((jug1, capacity_jug2))
        # Empty jug1
        q.put((0, jug2))
        # Empty jug2
        q.put((jug1, 0))
        # Pour jug1 to jug2
        pour_amount = min(jug1, capacity_jug2 - jug2)
        q.put((jug1 - pour_amount, jug2 + pour_amount))
        # Pour jug2 to jug1
        pour_amount = min(jug2, capacity_jug1 - jug1)
        q.put((jug1 + pour_amount, jug2 - pour_amount))

    return None

# Example usage
capacity_jug1 = 4
capacity_jug2 = 3
target = 2
result = water_jug_bfs(capacity_jug1, capacity_jug2, target)
print("Water Jug Solution:", result)
