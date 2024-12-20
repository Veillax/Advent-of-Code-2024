from collections import Counter

def compare(left_list, right_list):
    """Calculates the similarity score between two lists."""

    right_counts = Counter(right_list)  # Count occurrences in the right list
    score = 0

    for num in left_list:
        score += num * right_counts[num]

    return score

left_list, right_list = [], []

f = open("input.txt", "r", encoding="utf-8")

for line_number, line in enumerate(f.readlines(), 1):  # Start line numbering from 1
    print(f"\rReading line {line_number}: {line.strip()}", end="")  # Print the line being read
    left_list.append(int(line.split("   ")[0]))
    right_list.append(int(line.split("   ")[1]))

left_list.sort()
right_list.sort()

print(f"\n{compare(left_list, right_list)}")