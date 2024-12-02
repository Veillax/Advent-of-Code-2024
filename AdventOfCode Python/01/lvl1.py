left_list, right_list = [], []

f = open("input.txt", "r", encoding="utf-8")

for line_number, line in enumerate(f.readlines(), 1):  # Start line numbering from 1
    print(f"\rReading line {line_number}: {line.strip()}", end="")  # Print the line being read
    left_list.append(int(line.split("   ")[0]))
    right_list.append(int(line.split("   ")[1]))

left_list.sort()
right_list.sort()

total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print("\n" + str(total_distance))