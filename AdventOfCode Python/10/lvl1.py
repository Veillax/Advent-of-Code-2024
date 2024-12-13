from collections import deque, defaultdict

# Read the input file
with open("input.txt", "r", encoding="utf-8") as f:
    input_map = [list(line.strip()) for line in f.readlines()]

# Define possible movement directions
directions = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0)
}

def is_valid_position(x, y):
    """Check if the position is within the map boundaries."""
    return 0 <= y < len(input_map) and 0 <= x < len(input_map[y])

def count_paths_to_nine():
    """Count paths from each '0' to '9'."""
    # Dictionary to store path counts for each '0'
    zero_path_counts = defaultdict(int)
    
    # Find all '0' positions
    zero_positions = [(x, y) for y in range(len(input_map)) 
                            for x in range(len(input_map[y])) 
                            if input_map[y][x] == '0']
    
    for start_x, start_y in zero_positions:
        # Queue for BFS
        queue = deque([(start_x, start_y, 0)])
        
        # Track visited positions to prevent revisiting
        visited = set([(start_x, start_y)])
        
        while queue:
            current_x, current_y, current_value = queue.popleft()
            
            # Check each adjacent position
            for direction, (dx, dy) in directions.items():
                next_x, next_y = current_x + dx, current_y + dy
                
                # Check if next position is valid
                if not is_valid_position(next_x, next_y):
                    continue
                
                # Get the value of the next position
                next_value = input_map[next_y][next_x]
                
                # Skip if already visited
                if (next_x, next_y) in visited:
                    continue
                
                # Check if the next value is the next number in sequence
                if next_value == str(current_value + 1):
                    # If we've reached '9', increment the path count
                    if next_value == '9':
                        zero_path_counts[(start_x, start_y)] += 1
                    
                    # Add to queue and mark as visited
                    queue.append((next_x, next_y, current_value + 1))
                    visited.add((next_x, next_y))
    
    return zero_path_counts

# Calculate and print the path counts
path_counts = count_paths_to_nine()
print("Path counts from '0' to '9':")
scores = 0
for (x, y), count in path_counts.items():
    print(f"Starting from '0' at ({x}, {y}): {count} paths to '9'")
    scores += count
    
print(scores)