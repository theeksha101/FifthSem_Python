emot = ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC',
        'DIV', 'READ', 'PRINT', 'START', 'END', 'ORIGIN', 'EQU', 'LTORG',
        'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GE', 'NE',
        'LE', 'GT', 'ANY']
print(len(emot))

file = open('code.txt', 'r')
symbol_table = []

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    if split_string[0] not in emot:
        symbol_table.append(split_string[0])

print(symbol_table)
file.close()