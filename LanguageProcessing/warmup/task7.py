input_for_file = [input("Enter conditions") for i in range(2)]
file = open('scatchfile2.txt', 'r')

# print(input_for_file[0][0])
symbol_set = {}
line_count = 1

for line in file:
    index = []
    for i in range(len(input_for_file)):
        for j in range(len(input_for_file[i])):
            if input_for_file[i][j] in line:
                index.append(line.index(input_for_file[i][j]))
    if len(index) == 2:
        print('Line ', line_count, ': ', line[index[0] + 1: index[1]])
    elif len(index) == 1:
        print('Line ', line_count, ': ', line[index[0]])
    else:
        print('Line ', line_count, ': ')
    line_count += 1