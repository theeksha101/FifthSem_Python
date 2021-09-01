file_name = input("Enter File Name")
file = open(file_name + ".txt", 'r')
list_string = []
for line in file:
    list_string = line.split()
    print(len(list_string))
file.close()
