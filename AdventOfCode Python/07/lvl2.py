import concurrent.futures

puzzle_input = [line.strip() for line in open("input.txt", "r", encoding="utf-8").readlines()]

count = 0

def trin(num):
    if num == 0:
        return '0'
    trinary = ''
    while num > 0:
        remainder = num % 3
        trinary = str(remainder) + trinary
        num //= 3
    return trinary

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
            elif current_operator == "|":
                result = int(f"{result}{current_number}")

            current_operator = char
            current_number = 0

    if current_operator == '+':
        result += current_number
    elif current_operator == '*':
        result *= current_number
    elif current_operator == "|":
        result = int(f"{result}{current_number}")

    return result

def get_sequences(count):
    sequences = []
    for sequence in range(3**count - 1, -1, -1):
        trinary_str = trin(sequence).zfill(count)
        sequences.append(trinary_str.replace("0", "+").replace("1", "*").replace("2", "|"))
    return sequences

def process(equation):
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

def process_equations(puzzle_input):
    global count
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        results = executor.map(process, puzzle_input)
        
        for result in results:
            if result[0]:
                count += result[2]
                print(result[2], "=", result[1])

process_equations(puzzle_input)

print(count)