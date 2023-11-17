#Python | Ways to remove a key from dictionary
user_dict={}
num=int(input("Enter your number of dictionaries :"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    user_dict[key]=value
print("User Dictionary:",user_dict)
key=input(" Enter your key from the dictionary you would like to delete")
new_dict = {key: val for key,  val in user_dict.items() if key != key}
print("Your removal of key from the dictionary is:",new_dict)