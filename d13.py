#Python – Key with maximum unique values
user_dict={}
num=int(input("Enter your number of dictionaries with lists:"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:").split(',')
    values=[v.strip() for v in value]
    user_dict[key]=value
print("User Dictionary:",user_dict)

max_value=0
max_key=None
for x in user_dict:
     if len(set(user_dict[x]))>max_value:
          max_value=len(set(user_dict[x]))
          max_key=x
print("Key with  maximum unique values:",max(max_key))          
