n = int(input("Enter number of processes: "))

p = []

for i in range(n):
    name = input("Process: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))

    p.append({
        "name": name,
        "at": at,
        "bt": bt,
        "index": i
    })


time = 0
done = []
np_result = []
np_sequence = []

while len(done) < n:

    ready = []

    for x in p:
        if x not in done and x["at"] <= time:
            ready.append(x)

    if not ready:
        time += 1
        continue

    current = min(
        ready,
        key=lambda x: (x["bt"], x["at"], x["index"])
    )

    time += current["bt"]

    ct = time
    tat = ct - current["at"]
    wt = tat - current["bt"]

    np_result.append({
        "name": current["name"],
        "at": current["at"],
        "bt": current["bt"],
        "ct": ct,
        "tat": tat,
        "wt": wt,
        "index": current["index"]
    })

    np_sequence.append(current["name"])

    done.append(current)


print("Execution Sequence:", " ".join(np_sequence))

print("\n{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
    "PID", "AT", "BT", "CT", "TAT", "WT"
))

for x in sorted(np_result, key=lambda x: x["index"]):

    print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
        x["name"],
        x["at"],
        x["bt"],
        x["ct"],
        x["tat"],
        x["wt"]
    ))

np_total_tat = sum(x["tat"] for x in np_result)
np_total_wt = sum(x["wt"] for x in np_result)

np_avg_tat = np_total_tat / n
np_avg_wt = np_total_wt / n

print("\nAverage TAT =", np_avg_tat)
print("Average WT =", np_avg_wt)

remaining = []

for x in p:
    remaining.append({
        "name": x["name"],
        "at": x["at"],
        "bt": x["bt"],
        "remaining": x["bt"],
        "ct": 0,
        "index": x["index"]
    })

time = 0
completed = 0
pre_sequence = []

while completed < n:

    ready = []

    for x in remaining:
        if x["at"] <= time and x["remaining"] > 0:
            ready.append(x)

    if not ready:
        time += 1
        continue

    
    current = min(
        ready,
        key=lambda x: (x["remaining"], x["at"], x["index"])
    )

    
    if len(pre_sequence) == 0 or pre_sequence[-1] != current["name"]:
        pre_sequence.append(current["name"])

    current["remaining"] -= 1
    time += 1

    
    if current["remaining"] == 0:
        current["ct"] = time
        completed += 1


pre_result = []

for x in remaining:

    ct = x["ct"]
    tat = ct - x["at"]
    wt = tat - x["bt"]

    pre_result.append({
        "name": x["name"],
        "at": x["at"],
        "bt": x["bt"],
        "ct": ct,
        "tat": tat,
        "wt": wt,
        "index": x["index"]
    })
print("Execution Sequence:", " ".join(pre_sequence))

print("\n{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
    "PID", "AT", "BT", "CT", "TAT", "WT"
))

for x in sorted(pre_result, key=lambda x: x["index"]):

    print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
        x["name"],
        x["at"],
        x["bt"],
        x["ct"],
        x["tat"],
        x["wt"]
    ))

pre_total_tat = sum(x["tat"] for x in pre_result)
pre_total_wt = sum(x["wt"] for x in pre_result)

pre_avg_tat = pre_total_tat / n
pre_avg_wt = pre_total_wt / n

print("\nAverage TAT =", pre_avg_tat)
print("Average WT =", pre_avg_wt)
print("\nAverage Waiting Time:")
print("Non-Preemptive SJF = {:.2f}".format(np_avg_wt))
print("Preemptive SJF     = {:.2f}".format(pre_avg_wt))
print("\nAverage Turnaround Time:")
print("Non-Preemptive SJF = {:.2f}".format(np_avg_tat))
print("Preemptive SJF     = {:.2f}".format(pre_avg_tat))