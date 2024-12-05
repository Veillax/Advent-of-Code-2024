f = open("input.txt", "r", encoding="utf-8")
grid = [line.strip() for line in f.readlines()]
f.close()

rows = len(grid)
cols = len(grid[0])
directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right Diagonal
    (-1, -1), # Up-Left Diagonal
    (1, -1),  # Down-Left Diagonal
    (-1, 1),  # Up-Right Diagonal
]
count = 0

def validate(x, y):
    return 0 <= x < rows and 0 <= y < cols

def check(x, y, dx, dy):
    for i in range(len("XMAS")):
        nx, ny = x + i * dx, y + i * dy
        if not validate(nx, ny) or grid[nx][ny] != 'XMAS'[i]:
            return False
    return True

for col in range(cols):
    for row in range(rows):
        for dx, dy in directions:
            if check(row, col, dx, dy):
                count += 1

print("Found patterns:", count)
