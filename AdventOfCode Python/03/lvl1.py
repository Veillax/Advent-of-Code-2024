import re
regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
f = open("input.txt", "r", encoding="utf-8")
matches = re.findall(regex, f.read())
digits = [list(map(int, m[4:-1].split(",")))  for m in matches]
mul_digits = [digit[0] * digit[1] for digit in digits]
total = sum(mul_digits)
print(total)