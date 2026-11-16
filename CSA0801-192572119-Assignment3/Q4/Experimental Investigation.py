import time
for n in [10000, 100000, 1000000]:
    data = list(range(n))
    s = set(data)
    start = time.perf_counter()
    x = n - 1 in data
    list_time = time.perf_counter() - start
    start = time.perf_counter()
    x = n - 1 in s
    set_time = time.perf_counter() - start
    print("\nElements:", n)
    print("List search:", list_time)
    print("Set search:", set_time)
# Common students comparison
a = set(range(10000))
b = set(range(5000, 15000))
start = time.perf_counter()
common = a & b
print("Set intersection time:", time.perf_counter() - start)
start = time.perf_counter()
common_list = [x for x in a for y in b if x == y]
print("Nested loop time:", time.perf_counter() - start)
print("Common students:", sorted(common))
