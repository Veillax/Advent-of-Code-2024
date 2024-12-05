import re

# Read the input file
with open('input.txt', 'r', encoding='utf-8') as file:
    grid = file.read().splitlines()

# Define the size of the grid
rows = len(grid)
cols = len(grid[0])
count = 0

# Validity check to ensure coordinates are within bounds
def valid(x, y):
    return 0 <= x < cols and 0 <= y < rows

patterns = [
    [
        ["M", "M"],
        ["A"],
        ["S", "S"],
    ],
    [
        ["M", "S"],
        ["A"],
        ["M", "S"],
    ],
    [
        ["S", "S"],
        ["A"],
        ["M", "M"],
    ],
    [
        ["S", "M"],
        ["A"],
        ["S", "M"],
    ],
]

def check(x, y):
    m = [
        [grid[y][x], grid[y][x+2]],
        [grid[y+1][x+1]],
        [grid[y+2][x], grid[y+2][x+2]],        
    ]
    
    if m not in patterns:
        return False
    return True

for row in range(rows - 2):
    for col in range(cols - 2):
        if check(col, row):
            count += 1

print(count)