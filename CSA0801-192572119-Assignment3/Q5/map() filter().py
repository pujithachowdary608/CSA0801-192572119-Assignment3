readings = [10, 20, 30, -60, 5, 8, 55, 2, 12, 0]
valid = list(filter(lambda c: -50 <= c <= 50, readings))
fahrenheit = list(map(lambda c: c * 9/5 + 32, valid))
print("Valid:", valid)
print("Fahrenheit:", fahrenheit)
