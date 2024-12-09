def parse_map(input_map):
    antennas = []
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != ".":
                antennas.append((x, y, char))
    return antennas

def find_harmonic_antinodes(antennas, width, height):
    antinodes = set()
    freq_groups = {}

    # Group antennas by frequency
    for x, y, freq in antennas:
        freq_groups.setdefault(freq, []).append((x, y))

    for freq, points in freq_groups.items():
        # All antennas of this frequency are antinodes
        antinodes.update(points)

        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Compute the direction vector
                dx = x2 - x1
                dy = y2 - y1

                # Reduce vector to smallest integer steps
                gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(__import__("math").gcd(dx, dy))
                dx //= gcd
                dy //= gcd

                # Traverse along the line formed by the two points
                x, y = x1, y1
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy

                x, y = x2, y2
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x += dx
                    y += dy

    return antinodes

def count_unique_antinodes(input_map):
    width = len(input_map[0])
    height = len(input_map)
    antennas = parse_map(input_map)
    antinodes = find_harmonic_antinodes(antennas, width, height)

    # Mark antinodes on the map
    updated_map = list(input_map)
    for x, y in antinodes:
        updated_map[y] = updated_map[y][:x] + "#" + updated_map[y][x+1:]

    return len(antinodes), updated_map

input_map = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

#input_map = ["............","........0...",".....0......",".......0....","....0.......","......A.....","............","............","........A...",".........A..","............","............"]

# Calculate and print the result
result = count_unique_antinodes(input_map)
print("Unique antinode locations:", result[0])
print("Map (With antinodes marked)")
for line in result[1]:
    print(line)