# Lab 3 - Water Jug Problem solved using Depth First Search (DFS)

# Capacities of jugs
capacity_jug1 = 4
capacity_jug2 = 3

# Required target in Jug1
goal_amount = 2

# To keep track of visited states
visited = set()

def display(step_no, action, x, y):
    print(f"Step {step_no}: {action}")
    print(f"        Jug1 = {x} liters | Jug2 = {y} liters\n")

def dfs(j1, j2, step):
    
    # Goal condition
    if j1 == goal_amount:
        print("🎯 Goal Achieved Successfully!")
        return True
    
    # If already visited, skip
    if (j1, j2) in visited:
        return False
    
    visited.add((j1, j2))
    
    # ---- Possible Operations ----
    
    # 1. Fill Jug1 completely
    if dfs_operation(step, "Fill Jug1", capacity_jug1, j2):
        return True
    
    # 2. Fill Jug2 completely
    if dfs_operation(step, "Fill Jug2", j1, capacity_jug2):
        return True
    
    # 3. Empty Jug1
    if dfs_operation(step, "Empty Jug1", 0, j2):
        return True
    
    # 4. Empty Jug2
    if dfs_operation(step, "Empty Jug2", j1, 0):
        return True
    
    # 5. Transfer water from Jug1 to Jug2
    transfer = min(j1, capacity_jug2 - j2)
    if dfs_operation(step, "Pour Jug1 → Jug2", j1 - transfer, j2 + transfer):
        return True
    
    # 6. Transfer water from Jug2 to Jug1
    transfer = min(j2, capacity_jug1 - j1)
    if dfs_operation(step, "Pour Jug2 → Jug1", j1 + transfer, j2 - transfer):
        return True
    
    return False

def dfs_operation(step, rule, new_j1, new_j2):
    if (new_j1, new_j2) not in visited:
        display(step, rule, new_j1, new_j2)
        return dfs(new_j1, new_j2, step + 1)
    return False


# ---- Execution Starts Here ----
print("Water Jug Problem Using DFS")
print("=" * 40)
print(f"Jug1 Capacity : {capacity_jug1} liters")
print(f"Jug2 Capacity : {capacity_jug2} liters")
print(f"Target Amount : {goal_amount} liters in Jug1")
print("=" * 40)

display(0, "Initial State", 0, 0)
dfs(0, 0, 1)