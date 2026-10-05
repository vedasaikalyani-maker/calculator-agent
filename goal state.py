temp = int(input("Enter current temperature: "))

goal = 72

if temp > goal:
    print("Action: Cool")
elif temp < goal:
    print("Action: Heat")
else:
    print("Goal reached: Temperature is 72")