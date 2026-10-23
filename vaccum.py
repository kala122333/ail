def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    else:
        if location == "A":
            return "Move Right"
        else:
            return "Move Left"

rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

print("Initial Environment:", rooms)

while "Dirty" in rooms.values():
    status = rooms[location]
    action = vacuum_agent(location, status)

    print("Location:", location, "| Status:", status, "| Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"

print("Final Environment:", rooms)
print("All rooms are clean!")