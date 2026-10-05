def temperature_agent(temp, goal=72, max_iters=10):

    for i in range(max_iters):
        # Observe
        print("Observation:", temp)

        # Check goal
        if temp == goal:
            print("Goal reached!")
            return "success"

        # Decide
        if temp > goal:
            action = "Cool"
        else:
            action = "Heat"

        print("Decision:", action)

        # Act
        if action == "Cool":
            temp -= 10
        else:
            temp += 10

        print("After action:", temp)
        print("----------------")

    return "failure"


result = temperature_agent(120)

print("Result:", result)