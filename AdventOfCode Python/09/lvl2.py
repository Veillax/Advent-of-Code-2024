def onLoopEnd():
    print("MAX ITERATIONS REACHED")

with open("input.txt", "r", encoding="utf-8") as f:
    input_str = f.read().strip()

# input_str = "2333133121414131402"

# Parse the input into blocks
def parse_blocks(input_str):
    blocks = []
    space_idx = []
    space_count = 0
    block_type = 0  # 0: space, 1: file
    file_id = 0

    for count in map(int, input_str):
        if block_type == 0:  # File block
            blocks.append({
                'type': 1,  # File type
                'files': [file_id] * count,
                'space_length': 0
            })
            file_id += 1
        else:  # Space block
            if count > 0:
                space_count += count
                space_idx.append(len(blocks))
                blocks.append({
                    'type': 0,  # Space type
                    'files': [],
                    'space_length': count
                })
        
        block_type = 1 - block_type  # Toggle between 0 and 1

    return blocks, space_count, space_idx

# Solve part 2
def solve_part2(input_str):
    blocks, space_count, space_idx = parse_blocks(input_str)
    
    curr_block_idx = len(blocks) - 1

    while curr_block_idx > 0:
        if blocks[curr_block_idx]['type'] == 0:  # Skip space blocks
            curr_block_idx -= 1
            continue

        curr_block_len = len(blocks[curr_block_idx]['files'])
        
        for curr_space_idx in space_idx:
            if curr_space_idx >= curr_block_idx:
                break

            if blocks[curr_space_idx]['space_length'] >= curr_block_len:
                # Move files to the space block
                blocks[curr_space_idx]['files'].extend(blocks[curr_block_idx]['files'])
                blocks[curr_space_idx]['space_length'] -= curr_block_len

                # Convert current block to space block
                blocks[curr_block_idx]['type'] = 0
                blocks[curr_block_idx]['space_length'] = curr_block_len
                blocks[curr_block_idx]['files'] = []

                # Remove space index if space is filled
                if blocks[curr_space_idx]['space_length'] == 0:
                    space_idx.remove(curr_space_idx)

                break

        curr_block_idx -= 1

    # Calculate checksum
    checksum = 0
    pos = 0
    for block in blocks:
        for file in block['files']:
            checksum += pos * file
            pos += 1
        if block['type'] == 0:  # If space block
            pos += block['space_length']

    return checksum

# Calculate and print result
print("Calculating checksum")
result = solve_part2(input_str)
print({"checksum": result})