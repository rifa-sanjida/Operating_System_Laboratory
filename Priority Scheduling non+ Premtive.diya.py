n = int(input("Enter number of processes: "))
p = []

for i in range(n):
    print("\nProcess", i + 1)

    id = input("P_ID: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    pr = int(input("Priority: "))

    p.append({
        "id": id,
        "at": at,
        "bt": bt,
        "pr": pr
    })

print("\nNON-PREEMPTIVE PRIORITY")

t = 0
done_count = 0
done = [False] * n

ct = [0] * n
tat = [0] * n
wt = [0] * n

while done_count < n:

    sel = -1

    for i in range(n):
        if not done[i] and p[i]["at"] <= t:

            if sel == -1:
                sel = i

            elif p[i]["pr"] < p[sel]["pr"]:
                sel = i

    if sel == -1:
        t += 1
        continue

    t += p[sel]["bt"]

    ct[sel] = t
    tat[sel] = ct[sel] - p[sel]["at"]
    wt[sel] = tat[sel] - p[sel]["bt"]

    done[sel] = True
    done_count += 1

print("\nP_ID\tAT\tBT\tPR\tCT\tTAT\tWT")

sum_tat = 0
sum_wt = 0

for i in range(n):

    print(
        p[i]["id"], "\t",
        p[i]["at"], "\t",
        p[i]["bt"], "\t",
        p[i]["pr"], "\t",
        ct[i], "\t",
        tat[i], "\t",
        wt[i]
    )

    sum_tat += tat[i]
    sum_wt += wt[i]

print("\nAverage TAT =", sum_tat / n)
print("Average WT  =", sum_wt / n)

print("\nPREEMPTIVE PRIORITY")

rem = []

for i in range(n):
    rem.append(p[i]["bt"])

ct2 = [0] * n
tat2 = [0] * n
wt2 = [0] * n

t = 0
done_count = 0

while done_count < n:
    sel = -1

    for i in range(n):

        if rem[i] > 0 and p[i]["at"] <= t:

            if sel == -1:
                sel = i

            elif p[i]["pr"] < p[sel]["pr"]:
                sel = i

    if sel == -1:
        t += 1
        continue

    rem[sel] -= 1
    t += 1

    if rem[sel] == 0:

        ct2[sel] = t
        tat2[sel] = ct2[sel] - p[sel]["at"]
        wt2[sel] = tat2[sel] - p[sel]["bt"]

        done_count += 1


print("\nP_ID\tAT\tBT\tPR\tCT\tTAT\tWT")

sum_tat = 0
sum_wt = 0

for i in range(n):

    print(
        p[i]["id"], "\t",
        p[i]["at"], "\t",
        p[i]["bt"], "\t",
        p[i]["pr"], "\t",
        ct2[i], "\t",
        tat2[i], "\t",
        wt2[i]
    )

    sum_tat += tat2[i]
    sum_wt += wt2[i]

print("\nAverage TAT =", sum_tat / n)
print("Average WT  =", sum_wt / n)