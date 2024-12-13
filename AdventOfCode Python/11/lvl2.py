import time

start_time = time.time()

# Use a dictionary to store stone counts
content = {
    1950139: 1,
    0: 1,
    3: 1,
    837: 1,
    6116: 1,
    18472: 1,
    228700: 1,
    45: 1
}

def blink(content):
    updated_content = {}
    for x, count in content.items():
        if x == 0:
            updated_content[1] = updated_content.get(1, 0) + count
        elif len(str(x)) % 2 == 0:
            divisor = 10**(len(str(x)) // 2)
            left_half = x // divisor
            right_half = x % divisor
            updated_content[left_half] = updated_content.get(left_half, 0) + count
            updated_content[right_half] = updated_content.get(right_half, 0) + count
        else:
            updated_content[x * 2024] = updated_content.get(x * 2024, 0) + count
    return updated_content

print(f"Starting with {sum(content.values())} stones")

for i in range(75):
    blink_start_time = time.time()
    content = blink(content)
    blink_end_time = time.time()
    elapsed_time = blink_end_time - blink_start_time
    print(f"(Blink {i+1}) There are {sum(content.values())} stones, took {elapsed_time:1f} seconds")

elapsed_time = time.time() - start_time
print(f"There are {sum(content.values())} stones, took {elapsed_time:1f} seconds")