def check(arr):
    increasing = arr[1] > arr[0]
    decreasing = arr[1] < arr[0]

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if abs(diff) not in [1, 2, 3]:
            return False
        if (increasing and diff < 0) or (decreasing and diff > 0):
            return False

    return True

lines = []
safe = 0

f = open("input.txt", "r", encoding="utf-8")

for line_number, line in enumerate(f.readlines(), 1):
    print(f"\rReading line {line_number}: {line.strip()}", end="")
    l = line.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    lines.append(l)

for line in lines:
    if check(line):
        safe += 1

print(f"\n{safe}")