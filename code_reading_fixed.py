temperature = 120
goal = 72
max_iters = 10

log = []

for step in range(max_iters):
    print("Step:", step + 1)
    print("Temperature:", temperature)

    if temperature > goal:
        action = "Cool"
        temperature = max(goal, temperature - 10)
    elif temperature < goal:
        action = "Heat"
        temperature = min(goal, temperature + 10)
    else:
        action = "Goal Reached"

    log.append({
        "step": step + 1,
        "action": action,
        "temperature": temperature
    })

    print("Action:", action)
    print("New Temperature:", temperature)
    print()

    if temperature == goal:
        print("Reached goal at step", step + 1)
        break

print("Final Temperature:", temperature)
print("Total Steps:", len(log))
print("Log:", log)