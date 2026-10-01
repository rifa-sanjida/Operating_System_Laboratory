n = int(input("enter number of req: "))

req = list(map(int,input("enter req sequence: ").split()))

head = int(input("enter head: "))

total_seek = 0
sequence = []

while req:
    nearest = min(req, key = lambda x: abs(head - x))
    distance = abs (head - nearest)

    total_seek += distance

    head = nearest
    sequence.append(nearest)
    req.remove(nearest)

print("\nSeek Sequence:", sequence)
print("Total Seek Time:", total_seek)