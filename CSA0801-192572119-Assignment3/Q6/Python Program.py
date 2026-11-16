trains = {
    101: {"name": "Chennai Express", "stops": [("Chennai", "06:00", "06:10"), ("Katpadi", "08:00", "08:05")], "days": {"Mon", "Wed", "Fri"}},
    102: {"name": "Pandian Express", "stops": [("Madurai", "07:00", "07:10"), ("Chennai", "12:00", "12:10")], "days": {"Tue", "Thu"}},
    103: {"name": "Vaigai Express", "stops": [("Chennai", "08:00", "08:10"), ("Trichy", "11:00", "11:05")], "days": {"Mon", "Tue"}},
    104: {"name": "Kovai Express", "stops": [("Coimbatore", "09:00", "09:10"), ("Chennai", "15:00", "15:10")], "days": {"Wed", "Fri"}},
    105: {"name": "Rockfort Express", "stops": [("Trichy", "10:00", "10:10"), ("Chennai", "16:00", "16:10")], "days": {"Mon", "Wed"}}
}
station = "Chennai"
day = "Mon"
result = []
for no, details in trains.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0] == station:
                result.append((no, details["name"], stop[2]))
result.sort(key=lambda x: x[2])
print("Trains stopping at", station, "on", day)
for train in result:
    print(train)
print("\nComplete Timetable:")
for no, details in trains.items():
    print(no, details["name"], details["stops"], details["days"])
