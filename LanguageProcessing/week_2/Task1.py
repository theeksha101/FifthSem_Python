from LanguageProcessing import Tries

keywords = Tries.Trie()

emot = ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC',
        'DIV', 'READ', 'PRINT', 'START', 'END', 'ORIGIN', 'EQU', 'LTORG',
        'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GE', 'NE',
        'LE', 'GT', 'ANY']

for keyword in emot:
    keywords.insert(keyword)

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

    if not keywords.search(split_string[0]):
        symbol_table[split_string[0]] = [lc, size]

    lc += size

print(symbol_table)
file.close()
