
input_string = "Enter some strings: "

list_string = input_string.split()

print("Fist letters of your  ")

for index in range(len(list_string)):
    list_string[index] = list_string[index][0]
print(list_string)