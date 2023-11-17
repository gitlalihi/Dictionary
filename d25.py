#Python – Dictionary Values Mean
user_dict={}
num=int(input("Enter your number of dictionaries with lists:"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    
    user_dict[key]=value
print("User Dictionary:",user_dict)
res = 0
for val in user_dict.values(): 
    res += val 
res = res / len(user_dict) 
print("The computed mean : " + str(res))  