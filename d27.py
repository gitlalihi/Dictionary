#Python – Maximum record value key in dictionary
user_dict={}
num=int(input("Enter your number of dictionaries with lists:"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    
    user_dict[key]=value
print("User Dictionary:",user_dict)
res = None
res_max = 0
for i in user_dict:
    if user_dict[i][key] > res_max:
        res_max = user_dict[i][key]
        res = i
   

print("The required key is : " + str(res))