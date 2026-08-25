n = int(input("enter processes: "))

p = []

for i in range(n):
    name = input("Process Name: ")
    arrival = int(input("Arrival Time: "))
    burst = int(input("Burst Time: "))

    p.append({
        "name": name,
        "at": arrival,
        "bt": burst,
        "rem": burst,
        "ct": 0
    })

quantum = int(input("Enter Time Quantum: "))

p.sort(key=lambda x: x["at"])

ready = []
time = 0
completed = 0

while completed < n:
    for i in range(n):
        if p[i]["at"] <= time and p[i]["rem"] > 0 and i not in ready:
            ready.append(i)

    if not ready:
        time += 1
        continue

    current = ready.pop(0)

    if p[current]["rem"] <= quantum:
        time += p[current]["rem"]
        p[current]["rem"] = 0

        p[current]["ct"] = time
        completed += 1

    else:
        p[current]["rem"] -= quantum
        time += quantum

    for i in range(n):
        if p[i]["at"] <= time and p[i]["rem"] > 0 and i not in ready:
            if i != current:
                ready.append(i)

    if p[current]["rem"] > 0:
        ready.append(current)

total_wt = 0
total_tat = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for x in p:

    tat = x["ct"] - x["at"]
    wt = tat - x["bt"]

    total_tat += tat
    total_wt += wt

    print(x["name"], "\t", x["at"], "\t", x["bt"],
          "\t", x["ct"], "\t", tat, "\t", wt)

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)