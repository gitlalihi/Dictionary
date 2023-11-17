#Python – Replace String by Kth Dictionary value
list=[]
num=int(input("Enter your number  in the list"))
for i in range(num):
    ele=input("Enter Your Element:")
    list.append(ele)
    
print("Your  original list is :",list)

user_dict={}
num=int(input("Enter your number of dictionaries :"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    user_dict[key]=value
print("User Dictionary:",user_dict)

K=3
for i in range(len(list)):
    if list[i] in user_dict:
        list[i] = user_dict[list[i]][K]
print("The list after substitution : " + str(list))