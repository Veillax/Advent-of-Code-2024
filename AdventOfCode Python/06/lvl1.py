def simulate_guard_path(map_data):
    # Parse the input map
    grid = [list(row) for row in map_data.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])

    # Directions: (row_offset, col_offset, symbol)
    directions = [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]

    # Find initial guard position and direction
    guard_pos = None
    direction_idx = None

    for r in range(rows):
        for c in range(cols):
            for idx, (_, _, symbol) in enumerate(directions):
                if grid[r][c] == symbol:
                    guard_pos = (r, c)
                    direction_idx = idx

    if guard_pos is None:
        raise ValueError("Guard starting position not found.")

    visited = set()

    def is_within_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    while True:
        r, c = guard_pos
        visited.add(guard_pos)

        # Determine next position
        dr, dc, _ = directions[direction_idx]
        next_r, next_c = r + dr, c + dc
        print("\r" + str(guard_pos) + ",", directions[direction_idx][2], end="")
        if is_within_bounds(next_r, next_c):
            if grid[next_r][next_c] == '#':
                # Turn right 90 degrees
                direction_idx = (direction_idx + 1) % 4
            else:
                # Move forward
                guard_pos = (next_r, next_c)

                if not is_within_bounds(next_r, next_c):
                    break
        else:
            break

    # Mark visited positions
    for r, c in visited:
        grid[r][c] = 'X'

    return len(visited), '\n'.join(''.join(row) for row in grid)

input_map = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

# Input map
input_map = """....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."""

# Simulate and display results
distinct_positions, final_map = simulate_guard_path(input_map)
print("\nDistinct Positions Visited:", distinct_positions)
print("Final Map:")
print(final_map)
