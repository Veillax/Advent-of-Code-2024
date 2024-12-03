def check(arr):
    if is_safe(arr):
        return True

    for i in range(len(arr)):
        temp_arr = arr[:i] + arr[i+1:]
        if is_safe(temp_arr):
            return True

    return False


def is_safe(arr):
    increasing = arr[1] > arr[0]
    decreasing = arr[1] < arr[0]

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if abs(diff) not in [1, 2, 3]:
            return False
        if (increasing and diff < 0) or (decreasing and diff > 0):
            return False

    return True

f = open("input.txt", "r", encoding="utf-8")

lines = []
safe = 0

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