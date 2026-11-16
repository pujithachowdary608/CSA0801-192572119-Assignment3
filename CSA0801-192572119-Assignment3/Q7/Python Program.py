import time
contacts = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
    {"name": "Ravi Kumar", "phone": "9840012345", "email": "ravi@yahoo.com"},
    {"name": "Priya", "phone": "9876543210", "email": "priya@gmail.com"},
    {"name": "Arun", "phone": "", "email": "arun@gmail.com"}
]
def normalize(number):
    return ''.join(c for c in number if c.isdigit())[-10:]
def merge(data):
    result = {}
    for c in data:
        number = normalize(c["phone"])
        if not number:
            continue
        if number not in result:
            result[number] = {
                "name": c["name"],
                "numbers": set(),
                "emails": set()
            }
        result[number]["numbers"].add(number)
        if c["email"]:
            result[number]["emails"].add(c["email"])
    return result
start = time.perf_counter()
merged = merge(contacts)
print("Merged contacts:")
for contact in merged.values():
    print(contact)
print("Time:", time.perf_counter() - start)
