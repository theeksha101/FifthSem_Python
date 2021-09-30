import re

symbol_table = {'L1': [202], 'NEXT': [207], 'BACK': [210], 'X': [219]}
symbol_table['L1'][0] = symbol_table['BACK'][0]
print(symbol_table)

emot = {1: {'STOP': 00, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP': 6,
            'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
        2: {'DS': 1, 'DC': 2},
        3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
        4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
        5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}
print(len(emot))
_class = {
    1: "IS",
    2: "DL",
    3: "AD",
    4: "RG",
    5: "CC"
}
print(emot[1]["MOVER"], "IS A MOVER OPCODE")
print(ord('9'))
# found_obj = None
# search_key = 1
# for obj in emot:
#     if obj == search_key:
#         found_obj = obj
#         print(found_obj)
#         raise ValueError("Keyword can not be label")
# else:
#     print('No object found.')

#
# literal_pattern = f"(.*)(='([0-9])')"
# line = "        ORIGIN L1+3 "
# match = re.match(literal_pattern, line)
# # string_literal = match.group(3)
# # print(int(string_literal))
# if re.match('.*ORIGIN', line):
#     origin_pattern = "\\s*(ORIGIN)\\s([a-zA-Z0-9]*)\\s(r'+')([0-9])"
#     match = re.match(origin_pattern, line)
#     if match:
#         match.groups()
#
