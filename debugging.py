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

            state["steps"] += 1

            log.append({
                "step": state["steps"],
                "temperature": observed_temp,
                "action": "Goal Reached"
            })

            return {
                "state": state,
                "log": log
            }

        if observed_temp > goal:
            action = "Cool"
        else:
            action = "Heat"

        # Validate action
        if action not in ["Cool", "Heat"]:
            return {
                "error": "Invalid action",
                "action": action,
                "state": state,
                "log": log
            }

        # Act
        if action == "Cool":
            state["temp"] -= 10
        elif action == "Heat":
            state["temp"] += 10

        # FIX: increment steps every iteration
        state["steps"] += 1

        # Log
        log.append({
            "step": state["steps"],
            "temperature": observed_temp,
            "action": action,
            "new_temperature": state["temp"]
        })

    # Maximum iterations exceeded
    state["status"] = "failure"

    return {
        "state": state,
        "log": log
    }


result = temperature_agent(120)

print("Final Result:")
print(result)