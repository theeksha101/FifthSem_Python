# Week3 Task2
# Generate Literal table and pool table and Symbol table
# Combine everything


emot = {1: {'STOP': 00, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP': 6,
            'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
        2: {'DS': 1, 'DC': 2},
        3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
        4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
        5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}

symbol_table = {}


def generate_symbol(_file):
    location_counter = _file.readline().split()
    lc = int(location_counter[1])
    size = 0

    for i in _file:
        replace_string = i.replace(',', ' ')
        split_string = replace_string.split()
        size = 1

        if split_string[0] == 'ORIGIN':
            plus_sign = split_string[1].index('+')
            variable = split_string[1][0:plus_sign]
            integer = int(split_string[1][-1])
            lc = symbol_table[variable][0] + integer

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
            if "EQU" in split_string:
                symbol_table[split_string[0]][0] = symbol_table[split_string[-1]][0]
        lc += size

    print(symbol_table)


def generate_literal(file_):
    list_literals = []
    location_counter = file_.readline().split()
    lc = int(location_counter[1])
    literal_table = {}
    pool_table = []
    index_lit = 0

    for i in file_:
        replace_string = i.replace(',', ' ')
        split_string = replace_string.split()
        if split_string[len(split_string) - 1][0] == '=':  # ['MOVER', 'AREG', "='5'"] --> split_string
            list_literals.append(split_string[len(split_string) - 1])  # storing only "='5'" in list_literals
        if split_string[0] == 'LTORG':
            pool_table.append(index_lit)
            while index_lit in range(index_lit, len(list_literals)):
                lit = list_literals[index_lit].replace('=', '')
                literal = lit.replace("'", "")
                literal_table[index_lit] = {lc: int(literal)}
                lc += 1
                index_lit += 1

        else:
            if split_string[0] == 'ORIGIN':
                plus_sign = split_string[1].index('+')
                variable = split_string[1][0:plus_sign]
                integer = int(split_string[1][-1])
                lc = symbol_table[variable][0] + integer
            else:
                lc += 1

    print(literal_table)
    print(pool_table)


if __name__ == '__main__':
    file2 = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_3/input_taks2.txt', 'r')
    generate_symbol(file2)
    file = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_3/input_taks2.txt', 'r')
    generate_literal(file)
    file.close()