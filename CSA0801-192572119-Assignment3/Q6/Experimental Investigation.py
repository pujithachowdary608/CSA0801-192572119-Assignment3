import random
import time
import sys
stations = ["Chennai", "Madurai", "Trichy", "Coimbatore"]
for n in [100, 1000, 10000]:
    data = {
        i: {
            "stops": [(random.choice(stations), "08:00", "08:10")
                      for _ in range(5)],
            "days": {"Mon", "Wed"}
        }
        for i in range(n)
    }
    start = time.perf_counter()
    for no, details in data.items():
        for stop in details["stops"]:
            if stop[0] == "Chennai":
                pass
    normal = time.perf_counter() - start
    index = {}
    for no, details in data.items():
        for stop in details["stops"]:
            index.setdefault(stop[0], []).append(no)
    start = time.perf_counter()
    result = index.get("Chennai", [])
    indexed = time.perf_counter() - start
    print("\nTrains:", n)
    print("Without index:", normal)
    print("With index:", indexed)
    print("Index memory:", sys.getsizeof(index))
