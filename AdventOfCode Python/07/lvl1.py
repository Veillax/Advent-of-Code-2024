puzzle_input = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

count = 0

def eval_expression(expression):
    result = 0
    current_number = 0
    current_operator = '+'
    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            if current_operator == '+':
                result += current_number
            elif current_operator == '*':
                result *= current_number
            current_operator = char
            current_number = 0

    # Handle the last number
    if current_operator == '+':
        result += current_number
    elif current_operator == '*':
        result *= current_number

    return result

def get_sequences(count):
    sequences = []
    for sequence in range(2**count - 1, -1, -1):
        binary_str = bin(sequence)[2:].zfill(count)
        sequences.append(binary_str.replace("0", "+").replace("1", "*"))
    return sequences

def process(equation):
    filled_equations = []
    correct_equations = []
    e = equation.split(": ")
    total = int(e[0])
    operands = e[1]
    operators = get_sequences(operands.count(" "))

    for sequence in operators:
        replacements_iter = iter(sequence)
        filled_eq = "".join(next(replacements_iter) if char == " " else char for char in operands)
        
        result = eval_expression(filled_eq)
        if result == total:
            return True, filled_eq, result

    return False, None

for x in puzzle_input:
    result = process(x)
    if result[0]:
        count += result[2]
        print(result[2], "=", result[1])

print(count)
