def temperature_agent(temp, goal=72, max_iters=10):

    state = {
        "temp": temp,
        "done": False,
        "steps": 0
    }

    while state["steps"] < max_iters:

        # Observe
        print("Observation:", state["temp"])

        # Decide
        if state["temp"] == goal:
            state["done"] = True
            return state

        if state["temp"] > goal:
            action = "Cool"
        else:
            action = "Heat"

        # Act
        if action == "Cool":
            state["temp"] -= 10
        else:
            state["temp"] += 10

        state["steps"] += 1

    return state


result = temperature_agent(120)

print("Final State:", result)