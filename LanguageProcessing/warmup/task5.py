entries = int(input("No of entries: "))

array = [[input("Enter Student Name"), input("Enter Student RollNo")] for i in range(entries)]

for i in array:
    print("Name: ", i[0])
    print("Roll Number: ", i[1])
    print("*************************")
