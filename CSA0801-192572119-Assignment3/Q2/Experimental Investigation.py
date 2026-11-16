import sys
import time
import copy
values = list(range(1000000))
t = tuple(values)
print("List memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(t))
start = time.perf_counter()
a = list(range(1000000))
print("List creation:", time.perf_counter() - start)
start = time.perf_counter()
b = tuple(range(1000000))
print("Tuple creation:", time.perf_counter() - start)
start = time.perf_counter()
x = a[500000]
print("List indexing:", time.perf_counter() - start)
start = time.perf_counter()
y = b[500000]
print("Tuple indexing:", time.perf_counter() - start)
data = ([1, 2], 3)
data[0].append(4)
print("Tuple containing list:", data)
