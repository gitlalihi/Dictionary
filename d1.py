#Python | Sort Python Dictionaries by Key or Value
user_dict = {}
num_entries = int(input("Enter the number of dictionary entries: "))
for i in range(num_entries):
   
    key = input("Enter key: ")
    value = input("Enter value: ")

    user_dict[key] = value

print("User Dictionary:", user_dict)

d=list(user_dict.keys())
d.sort()
sorted_dict={x:user_dict[x] for x in d}
print(sorted_dict)
