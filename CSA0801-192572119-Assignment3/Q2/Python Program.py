import copy
import sys
import time
# Tuple as dictionary key
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print("Stop:", stops[(13.0418, 80.2341)])
# Correct grid
rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7
print("Bad grid:", bad)
print("Good grid:", good)
print(bad[0] is bad[1], good[0] is good[1])
# Aliasing and copying
a = [[1, 2], [3, 4]]
alias = a
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 99
print("Original:", a)
print("Alias:", alias)
print("Shallow:", shallow)
print("Deep:", deep)
# Tuple unpacking
for lat, lon in stops:
    print(lat, lon)
