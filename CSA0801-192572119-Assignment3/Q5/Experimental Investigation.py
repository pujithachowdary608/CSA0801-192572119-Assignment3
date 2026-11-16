import time
import sys
import random
for n in [10000, 100000, 1000000]:
    readings = [random.randint(-60, 60) for _ in range(n)]
    start = time.perf_counter()
    a = [c for c in readings if -50 <= c <= 50]
    t1 = time.perf_counter() - start
    start = time.perf_counter()
    b = []
    for c in readings:
        if -50 <= c <= 50:
            b.append(c)
    t2 = time.perf_counter() - start
    start = time.perf_counter()
    c = list(filter(lambda x: -50 <= x <= 50, readings))
    t3 = time.perf_counter() - start
    print("\nReadings:", n)
    print("Comprehension:", t1)
    print("For loop:", t2)
    print("Filter:", t3)
generator = (x for x in readings if -50 <= x <= 50)
print("List memory:", sys.getsizeof(a))
print("Generator memory:", sys.getsizeof(generator))
print("Results equal:", a == b == c)
