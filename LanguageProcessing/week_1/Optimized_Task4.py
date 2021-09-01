from LanguageProcessing import Tries

keywords = Tries.Trie()

emot = ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC',
        'DIV', 'READ', 'PRINT', 'START', 'END', 'ORIGIN', 'EQU', 'LTORG',
        'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GE', 'NE',
        'LE', 'GT', 'ANY']

for keyword in emot:
    keywords.insert(keyword)

file = open('code.txt', 'r')

symbol_table = {}
location_counter = file.readline().split()
lc = int(location_counter[1])

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    if not keywords.search(split_string[0]):
        symbol_table[split_string[0]] = lc
    lc += 1

print(symbol_table)
file.close()

