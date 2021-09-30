
emot = {1: {'STOP': 0, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP': 6,
            'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
        2: {'DS': 1, 'DC': 2},
        3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
        4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
        5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}

emot_class = {1: "IS",
              2: "DL",
              3: "AD",
              4: "RG",
              5: "CC"}

list_literals = []
literal_table = {}
symbol_table = {}
pool_table = []
index_lit = 0

file = open("input_code.txt")
start_location = file.readline().split()
lc = int(start_location[-1])

for line in file:
    tokens_line = line.split()
    # tokens_line len() is 0 when there's space in code.txt
    if len(tokens_line) == 0:
        continue

    #  Evaluate ORIGIN
    elif tokens_line[0] == "ORIGIN":
        # 'evaluate_origin' is a list containing symbol and an integer
        evaluate_origin = tokens_line[1].split("+")
        # adding location of that symbol with integer from 'evaluate_origin'
        lc = symbol_table[evaluate_origin[0]][0] + int(evaluate_origin[1])

    #  making literal table
    elif tokens_line[-1][0] == "=":
        string_literal = tokens_line[-1]
        list_literals.append(string_literal.translate({ord(c): None for c in "='"}))

    #  Evaluate LTORG
    elif "LTORG" in tokens_line:
        pool_table.append(index_lit)
        while index_lit in range(index_lit, len(list_literals)):
            literal_table[index_lit] = {lc: int(list_literals[index_lit])}
            lc += 1
            index_lit += 1

    #  making symbol table


    #  Evaluate EQU
    if "EQU" in tokens_line:
        label = tokens_line[0]
        symbol_table[label][0] = symbol_table[tokens_line[-1]][0]

    lc += 1

print(list_literals)
print(literal_table)
print(symbol_table)
print(pool_table)
