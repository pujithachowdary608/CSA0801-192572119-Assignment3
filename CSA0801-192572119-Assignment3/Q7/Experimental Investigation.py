import time
for n in [1000, 100000]:
    data = [
        {
            "name": "User" + str(i),
            "phone": str(9000000000 + i),
            "email": "user@gmail.com"  }
        for i in range(n)  ]
    start = time.perf_counter()
    merge(data)
    print(n, "contacts:", time.perf_counter() - start)
