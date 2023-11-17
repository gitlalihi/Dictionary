#Python | Merging two Dictionaries
user_dict = {}
num_entries = int(input("Enter the number of dictionary entries: "))
for i in range(num_entries):
   
    key = input("Enter key: ")
    value = input("Enter value: ")

    user_dict[key] = value

print("User Dictionary:", user_dict)

user_dict1 = {}
num_entries1 = int(input("Enter the number of  your second dictionary entries: "))
for i in range(num_entries1):
   
    key1 = input("Enter key: ")
    value1 = input("Enter value: ")

    user_dict1[key1] = value1

print(" Second User Dictionary:", user_dict1)


merged_dict={**user_dict,**user_dict1}
print("Your merged dictionaries is:",merged_dict)
