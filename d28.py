#Python – Extract values of Particular Key in Nested Values
nested_dict = {}
outer_key = input("Enter the key for the outer dictionary: ")
nested_dict[outer_key] = {}
for i in range (1):
   inner_key = input(f"Enter the key for the inner dictionary under '{outer_key}': ")
   inner_value = input(f"Enter the value for the key '{inner_key}': ")
   nested_dict[outer_key][inner_key] = inner_value

print("User's Nested Dictionary:")
print(nested_dict)
temp = inner_value

res = [val[temp] for key, val in nested_dict.items() if temp in val]
 

print("The extracted values : " + str(res)) 