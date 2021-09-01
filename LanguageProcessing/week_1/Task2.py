file_name = input("Enter file name:")
file = open(file_name + '.txt', 'r')
print(file.read())
file.close()