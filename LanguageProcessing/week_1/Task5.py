file = open('literal_code.txt', 'r')
literal_table = []
location_counter = file.readline().split()
lc = int(location_counter[1])

for i in file:
    replace_string = i.replace(',', ' ')
    split_string = replace_string.split()
    if split_string[len(split_string) - 1][0] == '=':
        literal_table.append(split_string[len(split_string) - 1])

for literal in literal_table:
    print(literal)

file.close()
