import time

start_time = time.time()

f = open("input.txt", "r", encoding="utf-8")
content = f.read()

#content = "0 1 10 99 999"

content = [int(line) for line in content.split(" ")]

def blink(content):
    i = 0
    while i < len(content):
        x = content[i]
        if x == 0:
            content[i] = 1

        elif len(str(x)) % 2 == 0:
            x = str(x)
            midpoint = len(x) // 2
            left_half = int(x[:midpoint]) if x[:midpoint] else 0
            right_half = int(x[midpoint:]) if x[midpoint:] else 0
            content = content[:i] + [left_half, right_half] + content[i+1:]
            i += 1

        else:
            content[i] = x * 2024
        i += 1
    return content
        
print(f"Starting with {len(content)} stones")

for i in range(25):
    blink_start_time = time.time()
    content = blink(content)
    blink_end_time = time.time()
    elapsed_time = blink_end_time - blink_start_time
    print(f"(Blink {i+1}) There are {len(content)} stones, took {elapsed_time:1f} seconds")
    
elapsed_time = time.time() - start_time

print(f"There are {len(content)} stones, took {elapsed_time:1f} seconds")