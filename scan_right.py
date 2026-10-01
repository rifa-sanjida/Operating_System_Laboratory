req = list(map(int, input("Requests: ").split()))
head = int(input("Head: "))

left = [x for x in req if x < head]
right = [x for x in req if x >= head]

right.sort()
left.sort()

seq = right + left[::-1]

total = 0
cur = head

for x in seq:
    total += abs(cur - x)
    cur = x

print("Seek Sequence:", seq)
print("Total Seek Time:", total)