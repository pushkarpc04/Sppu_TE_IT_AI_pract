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

def get_input():
    capacity_jug1 = int(input("Enter capacity of jug 1: "))
    capacity_jug2 = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter the target amount of water: "))
    return capacity_jug1, capacity_jug2, target

def main():
    capacity_jug1, capacity_jug2, target = get_input()
    result = water_jug_bfs(capacity_jug1, capacity_jug2, target)
    if result:
        print("Water Jug Solution:", result)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
