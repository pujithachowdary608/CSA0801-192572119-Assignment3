import random
readings = [random.randint(-60, 60) for _ in range(10)]
# Using for loop
valid = []
for c in readings:
    if -50 <= c <= 50:
        valid.append(c)
# Using list comprehension
celsius = [c for c in readings if -50 <= c <= 50]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
# Alarm minutes
alarms = [i+1 for i, c in enumerate(celsius) if c < 2 or c > 8]
print("Readings:", readings)
print("Valid Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Alarm minutes:", alarms)
