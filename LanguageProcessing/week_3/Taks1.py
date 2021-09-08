# Week3 Task1
# Generate Literal table and pool table with LTORG

file = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_3/input_task1.txt', 'r')
list_literals = []
location_counter = file.readline().split()
lc = int(location_counter[1])
literal_table = {}
pool_table = []
index_lit = 0

for i in file:
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
        lc += 1
lc -= 1
print(lc)
print(list_literals)
print("index_lit", index_lit)
print(len(list_literals))
for j in range(index_lit, len(list_literals)):
    lit = list_literals[index_lit].replace('=', '')
    literal = lit.replace("'", "")
    literal_table[lc] = int(literal)
    lc += 1
print(literal_table)
print(pool_table)
file.close()

