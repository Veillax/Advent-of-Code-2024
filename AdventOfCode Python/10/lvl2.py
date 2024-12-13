from collections import deque, defaultdict
import sys

# Increase recursion limit and stack size for complex explorations
sys.setrecursionlimit(10000)

def read_input_map(filename):
    """Read the map from a file."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def is_valid_position(x, y, width, height):
    """Check if the position is within map boundaries."""
    return 0 <= x < width and 0 <= y < height

def find_trailheads(input_map):
    """Find all trailhead positions (where '0' exists)."""
    trailheads = []
    for y in range(len(input_map)):
        for x in range(len(input_map[y])):
            if input_map[y][x] == '0':
                trailheads.append((x, y))
    return trailheads

def find_trailhead_rating(input_map, start_x, start_y):
    """Calculate the rating of a specific trailhead."""
    width, height = len(input_map[0]), len(input_map)
    
    # Directions: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Set to track unique paths
    unique_paths = set()
    
    def explore_path(x, y, path, current_val):
        """Recursively explore paths from the starting point."""
        # If path reaches any '9', add the unique path
        if current_val == 9:
            # Use tuple for hashability to track unique paths
            unique_paths.add(tuple(path))
            return
        
        # Try all four directions
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            # Check boundary and path validity
            if not is_valid_position(next_x, next_y, width, height):
                continue
            
            # Convert to int for comparison
            next_val = int(input_map[next_y][next_x])
            
            # Path can only increase by 1
            if next_val == current_val + 1:
                # Create a new path to avoid modifying the original
                new_path = path + [(next_x, next_y)]
                explore_path(next_x, next_y, new_path, next_val)
    
    # Start exploration from the trailhead
    explore_path(start_x, start_y, [(start_x, start_y)], 0)
    
    return len(unique_paths)

def solve_trailhead_ratings(input_map):
    """Calculate ratings for all trailheads."""
    trailhead_ratings = []
    trailheads = find_trailheads(input_map)
    
    for x, y in trailheads:
        rating = find_trailhead_rating(input_map, x, y)
        trailhead_ratings.append(rating)
    
    return trailhead_ratings

# Read the input map
input_map = read_input_map('input.txt')

# Solve and print the results
ratings = solve_trailhead_ratings(input_map)
print("Trailhead Ratings:", ratings)
print("Sum of Trailhead Ratings:", sum(ratings))