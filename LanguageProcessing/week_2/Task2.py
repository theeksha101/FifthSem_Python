file = open('/home/diksha/PycharmProjects/FifthSem/LanguageProcessing/week_1/literal_code.txt', 'r')
literal_table = []
location_counter = file.readline().split()
lc = int(location_counter[1])

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    if split_string[len(split_string) - 1][0] == '=':
        literal_table.append(split_string[len(split_string) - 1])
    lc += 1
lc -= 1
for j in range(len(literal_table)):
    lit = literal_table[j].replace('=', '')
    literal = lit.replace("'", "")
    literal_table[j] = [lc, int(literal)]
    lc += 1
print(literal_table)
file.close()

