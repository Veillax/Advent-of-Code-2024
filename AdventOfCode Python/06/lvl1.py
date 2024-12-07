import time

start_time = time.time()  # Start timing

def simulate_guard_path(grid):
    # Directions: 0 = up, 1 = right, 2 = down, 3 = left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    # Find initial position and direction
    x, y = None, None
    direction = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                x, y = j, i
                direction = 0
                break
        if x is not None:
            break
    guard_pos_set = (x, y)
    
    # Track visited positions and directions
    visited = set([(x, y, direction)])  # Store position and direction
    grid_list = [list(row) for row in grid]
    
    while True:
        # Check if next position is blocked
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        
        # Check if next move is out of bounds or blocked
        if (next_x < 0 or next_x >= len(grid[0]) or 
            next_y < 0 or next_y >= len(grid) or 
            grid_list[next_y][next_x] == '#'):
            # Turn right
            direction = (direction + 1) % 4
        else:
            grid[y] = grid[y][:x] + "X" + grid[y][x+1:] 
            # Move forward
            x, y = next_x, next_y
            
            # Check if the current position and direction have been visited before (loop detection)
            if (x, y, direction) in visited:
                # Loop detected, break
                break
            visited.add((x, y, direction))
        
            # Check if guard is leaving the grid
            if x == 0 or x == len(grid[0])-1 or y == 0 or y == len(grid)-1:
                grid[y] = grid[y][:x] + "X" + grid[y][x+1:]
                print(f"Exited at ({x}, {y})")
                break
            
    with open("input_x.txt", "w", encoding="utf-8") as f:
        for i, row in enumerate(grid):
            if i == guard_pos_set[1]:
                row = row[:guard_pos_set[0]] + "^" + row[guard_pos_set[0]:]
            f.write("".join(row) + "\n")

    return len(visited)

# Read input from file
f = open("input.txt", "r", encoding="utf-8")
content = [line.strip() for line in f.readlines()]
f.close()

# Solve and print the result
elapsed_time = time.time() - start_time
print(f"Unique positions: {simulate_guard_path(content)}, elapsed time: {elapsed_time:.2f}")

