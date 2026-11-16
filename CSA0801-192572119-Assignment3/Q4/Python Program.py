ai = {"192311001", "192311004", "192311007", "192311009"}
iot = {"192311002", "192311004", "192311009", "192311010"}
both = ai & iot
exactly_one = ai ^ iot
all_registered = ai | iot
print("Both:", sorted(both))
print("Exactly one:", sorted(exactly_one))
print("All registered:", sorted(all_registered))
