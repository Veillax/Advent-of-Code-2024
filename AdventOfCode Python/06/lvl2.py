def simulate_guard_path(map_data, obstruction=None):
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

    # Add obstruction
    if obstruction:
        grid[obstruction[0]][obstruction[1]] = '#'

    while True:
        r, c = guard_pos

        # Detect loop
        if (guard_pos, direction_idx) in visited:
            return True  # Loop detected
        visited.add((guard_pos, direction_idx))

        # Determine next position
        dr, dc, _ = directions[direction_idx]
        next_r, next_c = r + dr, c + dc

        # Check for obstacle or boundary
        if not is_within_bounds(next_r, next_c) or grid[next_r][next_c] == '#':
            # Turn right 90 degrees
            direction_idx = (direction_idx + 1) % 4
        else:
            # Move forward
            guard_pos = (next_r, next_c)

        # Stop if the guard reaches an invalid state
        if not is_within_bounds(guard_pos[0], guard_pos[1]):
            break

    return False  # No loop detected

def find_obstruction_positions(map_data):
    grid = [list(row) for row in map_data.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])
    valid_positions = []

    for r in range(rows):
        for c in range(cols):
            # Test only open spaces for obstructions
            if grid[r][c] == '.':
                if simulate_guard_path(map_data, obstruction=(r, c)):
                    valid_positions.append((r, c))

    return valid_positions

input_map = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

# Input map
input_map = """....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."""

# Find obstruction positions
obstruction_positions = find_obstruction_positions(input_map)
print("Possible Obstruction Positions:", obstruction_positions)
print("Count:", len(obstruction_positions))