file_name = input("Enter File Name")
file = open(file_name + ".txt", 'r')
list_string = []

for line in file:
    list_string.append(line.split())

for lst in list_string:
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    print(lst)
