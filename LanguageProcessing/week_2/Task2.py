#  Week2 Task2 making Literal Table with 2 fields...
#  1. location counter
#  2. a literal converted into integer type.

file = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_1/literal_code.txt', 'r')
list_literals = []
location_counter = file.readline().split()
lc = int(location_counter[1])

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    if split_string[len(split_string) - 1][0] == '=':  # ['MOVER', 'AREG', "='5'"] --> split_string
        list_literals.append(split_string[len(split_string) - 1])
    lc += 1
lc -= 1
literal_table = {}
for j in range(len(list_literals)):
    lit = list_literals[j].replace('=', '')
    literal = lit.replace("'", "")
    literal_table[lc] = int(literal)
    lc += 1
print(literal_table)
file.close()
