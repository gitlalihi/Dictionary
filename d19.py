#Python – Replace words from Dictionary
s1=str(input("Enter your string:"))
user_dict={}
num=int(input("Enter your number of dictionaries :"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:")
    user_dict[key]=value
print("User Dictionary:",user_dict)

temp=s1.split()
res=[]
for word in temp:
    res.append(user_dict.get(word,word))
res=" ".join(res)  
print("Replaced strings is :",res)  