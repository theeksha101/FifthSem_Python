#  Week2 Task1 making Symbol Table with 3 fields

emot = {1: {'STOP': 00, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP':6,
            'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
        2: {'DS': 1, 'DC': 2},
        3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
        4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
        5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}


file = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_1/code.txt', 'r')

symbol_table = {}
location_counter = file.readline().split()
lc = int(location_counter[1])
size = 0

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    size = 1

    if "DS" in split_string:
        x = split_string[2].replace("'", "")
        size = int(x)
        lc += size
        symbol_table[split_string[0]] = [lc, size]
        lc += 1
        continue
    j = 1
    while j <= 5:
        if split_string[0] in emot[j]:
            break
        j += 1
    else:
        symbol_table[split_string[0]] = [lc, size]
    lc += size

print(symbol_table)
file.close()
