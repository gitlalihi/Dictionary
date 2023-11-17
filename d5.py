#Get size of a Dictionary in Python
user_dict = {}
num_entries = int(input("Enter the number of dictionary entries: "))
for i in range(num_entries):
   
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("User Dictionary:", user_dict)
print("The size of your dictionary  in bytes is ", str(user_dict.__sizeof__()))