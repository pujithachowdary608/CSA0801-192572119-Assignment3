import random
import time
from collections import Counter
words = ["seeds", "price", "fertiliser", "subsidy", "water"]
for n in [1000, 10000, 100000]:
    data = [random.choice(words) for _ in range(n)]
    start = time.perf_counter()
    counts = {}
    for word in data:
        counts[word] = counts.get(word, 0) + 1
    dict_time = time.perf_counter() - start
    start = time.perf_counter()
    result = {word: data.count(word) for word in set(data)}
    list_time = time.perf_counter() - start
    start = time.perf_counter()
    counter = Counter(data)
    counter_time = time.perf_counter() - start
    print("\nWords:", n)
    print("Dictionary:", dict_time)
    print("List count:", list_time)
    print("Counter:", counter_time)
