def parse_map(input_map):
    antennas = []
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != ".":
                antennas.append((x, y, char))
    return antennas

def find_antinodes(antennas, width, height):
    antinodes = set()

    # Group antennas by frequency
    freq_groups = {}
    for x, y, freq in antennas:
        freq_groups.setdefault(freq, []).append((x, y))

    for freq, points in freq_groups.items():
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Calculate potential antinodes
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Check if antinodes are within bounds
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)

    return antinodes

def count_unique_antinodes(input_map):
    width = len(input_map[0])
    height = len(input_map)
    antennas = parse_map(input_map)
    antinodes = find_antinodes(antennas, width, height)
    temp_map = input_map
    for antinode in antinodes:
        x = antinode[0]
        y = antinode[1]
        line = temp_map[y]
        temp_map[y] = line[:x] + "#" + line[x+1:]
    return len(antinodes), temp_map

input_map = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

#input_map = ["............","........0...",".....0......",".......0....","....0.......","......A.....","............","............","........A...",".........A..","............","............"]

# Calculate and print the result
result = count_unique_antinodes(input_map)
print("Unique antinode locations:", result[0])
print("Map (With antinodes marked)")
for line in result[1]:
    print(line)