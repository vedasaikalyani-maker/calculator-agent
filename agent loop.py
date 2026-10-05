temp = 120

for i in range(3):
    # Observe
    print("Observation:", temp)

    # Decide
    if temp > 72:
        action = "Cool"
    elif temp < 72:
        action = "Heat"
    else:
        action = "Idle"

    print("Decision:", action)

    # Act
    if action == "Cool":
        temp -= 20
    elif action == "Heat":
        temp += 20

    print("After action:", temp)
    print("----------------")