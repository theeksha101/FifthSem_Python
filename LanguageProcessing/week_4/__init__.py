import re

if __name__ == '__main__':
    emot = {1: {'STOP': 00, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP': 6,
                'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
            2: {'DS': 1, 'DC': 2},
            3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
            4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
            5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}
    _class = {
        1: "IS",
        2: "DL",
        3: "AD",
        4: "RG",
        5: "CC"
    }
    print(len(emot))
    output = open("output.txt", "w")
    if 'STOP' in emot[1]:
        a = _class[1]
        output.write(a)

    # symbol_and_keyword = "([a-zA-Z]+[0-9]*)\\s+([a-zA-Z]+)"
    # symbol = "[a-zA-Z]+[0-9]*"
    # keyword = "[a-zA-Z]+"
    # number = "[0-9]+"
    #
    # file = open("input_code.txt")
    # for line in file:
    #     assembly_pattern1 = re.compile(f"\\s*{symbol_and_keyword}\\s+({keyword})\\W\\s*\\W*({symbol}|{number})\\W*")
    #     assembly_pattern2 = re.compile(f"\\s*({keyword})\\s+({symbol}|{keyword})\\W\\s*\\W*({symbol}|{number})\\W*")
    #     assembly_pattern3 = re.compile(f"\\s*({keyword}|{number})\\s*({keyword})?")
    #
    #     four_string_pattern = assembly_pattern1.match(line)  # matches   " L1      MOVEM BREG, ='2'"
    #     three_string_pattern = assembly_pattern2.match(line)  # matches     "MOVEM AREG, X"
    #     two_string_pattern = assembly_pattern3.match(line)
    #
    #     if four_string_pattern:
    #         print(four_string_pattern.groups())
    #     elif three_string_pattern:
    #         print(three_string_pattern.groups())
    #     elif two_string_pattern:
    #         print(two_string_pattern.groups())
