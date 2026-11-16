import random
readings = [random.randint(0, 50) for _ in range(14)]
weekly = [sum(readings[ii+7]) for i in range(0, 14, 7)]
averages = [sum(readings[ii+7])7 for i in range(8)]
dry_days = [i+1 for i, x in enumerate(readings) if x == 0]
print(Readings, readings)
print(Weekly totals, weekly)
print(Wettest week, weekly.index(max(weekly)) + 1)
print(Driest week, weekly.index(min(weekly)) + 1)
print(Moving averages, averages)
print(Dry days, dry_days)
