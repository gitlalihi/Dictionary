#Python program to find the sum of all items in a dictionary
user_dict = {}
num_entries = int(input("Enter the number of dictionary entries: "))
for i in range(num_entries):
   
    key = input("Enter key: ")
    value = input("Enter value: ")

    user_dict[key] = value
print("User Dictionary:", user_dict)

def returnSum(user_dict):
 
    sum = 0
    for i in user_dict.values():
        sum = sum + i
 
    return sum
 
print("Sum :", returnSum(user_dict))