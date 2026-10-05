def temperature_agent(temp, goal=72, max_iters=10):

    state = {
        "temp": temp,
        "done": False,
        "steps": 0,
        "status": "running"
    }

    log = []

    while state["steps"] < max_iters:

        # Observe
        observed_temp = state["temp"]

        # Decide
        if observed_temp == goal:
            state["done"] = True
            state["status"] = "success"

            log.append({
                "step": state["steps"],
                "temperature": observed_temp,
                "action": "Goal Reached"
            })

            return state, log

        if observed_temp > goal:
            action = "Cool"
            state["temp"] -= 10
        else:
            action = "Heat"
            state["temp"] += 10

        # Update steps
        state["steps"] += 1

        # Log the step
        log.append({
            "step": state["steps"],
            "temperature": observed_temp,
            "action": action,
            "new_temperature": state["temp"]
        })

    # Max iterations exceeded
    state["status"] = "failure"

    return state, log


result, full_log = temperature_agent(120)

print("Final State:")
print(result)

print("\nFull Log:")
for step in full_log:
    print(step)