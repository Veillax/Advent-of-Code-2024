from collections import Counter

def compare(left_list, right_list):
    right_counts = Counter(right_list)
    similarity_score = 0

    for num in left_list:
        similarity_score += num * right_counts[num]

    return similarity_score


with open("input.txt", "r", encoding="utf-8") as f:    
    left_list, right_list = [], []

    for line_number, line in enumerate(f.readlines(), 1):  # Start line numbering from 1
        print(f"\rReading line {line_number}: {line.strip()}", end="")  # Print the line being read
        left_list.append(int(line.split("   ")[0]))
        right_list.append(int(line.split("   ")[1]))
        
    score = compare(left_list, right_list)

print(f"\n{score}")