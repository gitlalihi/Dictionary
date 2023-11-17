#Python dictionary with keys having multiple inputs

multi_input_dict = {}
name = input("Enter name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
key = (name, age)

multi_input_dict[key] = gender
name = input("Enter another name: ")
age = int(input("Enter another age: "))
gender = input("Enter another gender: ")
key = (name, age)

multi_input_dict[key] = gender
print("Resulting Dictionary:", multi_input_dict)
