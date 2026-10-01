req = list(map(int,input("enter req sequence: ").split()))
head = int(input("enter head: "))

left = [x for x in req if x<head]
right = [x for x in req if x>=head]

left.sort()
right.sort()

seq = left[::-1]+[0]+right

total = 0
cur = head
for x in seq:
    total+=abs(cur-x)
    cur = x

print("Seek Sequence:", seq)
print("Total Seek Sequence:", total)