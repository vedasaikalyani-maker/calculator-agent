def temperature_agent(temp, goal=72, max_iters=10):

    state = {
        "temp": temp,
        "done": False,
        "steps": 0,
        "status": "running"
    }

    while state["steps"] < max_iters:

        # Observe
        print("Observation:", state["temp"])

        # Decide
        if state["temp"] == goal:
            state["done"] = True
            state["status"] = "success"
            return state

        if state["temp"] > goal:
            action = "Cool"
            state["temp"] -= 10
        else:
            action = "Heat"
            state["temp"] += 10

        # Update steps
        state["steps"] += 1

        print("Action:", action)

    # Max iterations exceeded
    state["status"] = "failure"
    return state


result = temperature_agent(120)

print("Final State:", result)