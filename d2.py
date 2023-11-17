#Handling missing keys in Python dictionaries
user_dict = {}
num_entries = int(input("Enter the number of dictionary entries: "))
for i in range(num_entries):
   
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("User Dictionary:", user_dict)
user_key = input("Enter a key to retrieve from the dictionary: ")
value = user_dict.get(user_key, "Key not found")
print(f"The value for key '{user_key}' is: {value}")
value = user_dict[user_key] if user_key in user_dict else "Key not found"
print(f"The value for key '{user_key}' is: {value}")