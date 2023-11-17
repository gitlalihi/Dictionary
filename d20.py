#Python – Remove Dictionary Key Words
s1=input("Enter your String:")
user_dict={}
num=int(input("Enter your number of dictionaries :"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    user_dict[key]=value
print("User Dictionary:",user_dict)
for key in user_dict:
    if key in s1.split(' '):
        s1 = s1.replace(key, "")
 
# Printing result
print("The string after replace : " + str(s1))