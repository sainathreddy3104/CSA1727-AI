
from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == target or b == target:
            return True

        # Fill Jug A
        queue.append((capacity_a, b))
        # Fill Jug B
        queue.append((a, capacity_b))
        # Empty Jug A
        queue.append((0, b))
        # Empty Jug B
        queue.append((a, 0))
        # Pour Jug A into Jug B
        pour_to_b = min(a, capacity_b - b)
        queue.append((a - pour_to_b, b + pour_to_b))
        # Pour Jug B into Jug A
        pour_to_a = min(b, capacity_a - a)
        queue.append((a + pour_to_a, b - pour_to_a))

    return False

# Example usage
capacity_a = 4
capacity_b = 3
target = 2
result = water_jug_problem(capacity_a, capacity_b, target)
print("Can measure the target amount:", result)
