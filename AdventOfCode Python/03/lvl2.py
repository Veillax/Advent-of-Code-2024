import re
filename = 'input.txt'
with open(filename, 'r', encoding="utf-8") as f:
  content = f.read()
regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
matches = re.findall(regex, content)
total = 0
enabled = True
for match in matches:
  index = content.rfind("do()", 0, content.index(match))
  dont_index = content.rfind("don't()", 0, content.index(match))
  if dont_index > index:
    enabled = False
  elif index > dont_index:
    enabled = True
  if enabled:
    digits = [int(x) for x in match[4:-1].split(",")]
    total += digits[0] * digits[1]
print(total)