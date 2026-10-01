requests = [176, 51, 50, 40, 39, 100]
head = 35
total = 0

print("FCFS Disk Scheduling")

print("\nSequence:")
print(head, end=" -> ")

print("\n\nSeek Operations:")

for x in requests:
    move = abs(x - head)
    total += move

    print(f"{head} -> {x} = {move}")

    head = x
    print(head, end=" -> ")

print("\n\nTotal Head Movement =", total)
print("Total Seek Operations =", len(requests))