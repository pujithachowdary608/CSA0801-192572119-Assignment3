import random
import time
def naive(arr):
    return [sum(arr[i:i+7])/7 for i in range(len(arr)-6)]
def running_sum(arr):
    if len(arr) < 7:
        return []
    result = []
    total = sum(arr[:7])
    result.append(total / 7)
    for i in range(7, len(arr)):
        total += arr[i] - arr[i-7]
        result.append(total / 7)
    return result
for n in [365, 36500, 365000]:
    data = [random.randint(0, 50) for _ in range(n)]
    start = time.perf_counter()
    naive(data)
    naive_time = time.perf_counter() - start
    start = time.perf_counter()
    running_sum(data)
    running_time = time.perf_counter() - start
    print("\nReadings:", n)
    print("Naive time:", naive_time)
    print("Running sum time:", running_time)
print("Empty list:", running_sum([]))
print("Short list:", running_sum([2, 4, 6, 8]))
