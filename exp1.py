def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

print("Initial Environment:", rooms)

while "Dirty" in rooms.values():
    status = rooms[location]
    action = vacuum_agent(location, status)

    print(f"Location: {location}, Status: {status}, Action: {action}")

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

print("Final Environment:", rooms)
print("Both rooms are clean!")