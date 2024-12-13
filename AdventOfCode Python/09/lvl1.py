def onLoopEnd():
    print("MAX ITERATIONS REACHED")
    

with open("input.txt", "r", encoding="utf-8") as f:
    input_str = f.read().strip()

input_str = "2333133121414131402"

print("Calculating diskExpanded")
diskExpanded = []
for index, char in enumerate(input_str):
    isFreeSpace = (index + 1) % 2 == 0
    blockID = index // 2 
    diskExpanded.extend([blockID if not isFreeSpace else "."] * int(char))

def sortDisk(disk):
    firstSpaceIndex = disk.index(".")
    lastNumIndex = len(disk) - 1 - disk[::-1].index(next(block for block in reversed(disk) if isinstance(block, int)))
    while firstSpaceIndex < lastNumIndex:
        disk[firstSpaceIndex], disk[lastNumIndex] = disk[lastNumIndex], disk[firstSpaceIndex]
        try:
            firstSpaceIndex = disk.index(".", firstSpaceIndex)
        except ValueError:
            break
        try:
            lastNumIndex = len(disk) - 1 - disk[::-1].index(
                next(block for block in reversed(disk) if isinstance(block, int) and disk.index(block) < lastNumIndex)
            )
        except StopIteration:
            break
    return disk

print("Calculating diskSorted")
diskSorted = sortDisk(diskExpanded.copy()) 

print("Calculating checksum")
checksum = sum(index * ID for index, ID in enumerate(item for item in diskSorted if isinstance(item, int)))
print({"checksum": checksum, "disk_sorted": ''.join(x for x in diskSorted)})
# p1e == 1928
# 5237527536 < 90273982836 < p1 == 6346871685398
