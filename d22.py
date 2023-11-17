#Python – Remove duplicate values across Dictionary Values
user_dict={}
num=int(input("Enter your number of dictionaries with lists:"))
for i in range (num):
    key=input("Enter your key:")
    value=input("Enter your value:").split(',')
    values=[v.strip() for v in value]
    user_dict[key]=values
print("User Dictionary:",user_dict)
x=[]
for i in user_dict.keys():
    x.extend(user_dict[i])
y=[]
for j in x:
    if x.count(j)==1:
        y.append(j)
res=dict
for i in user_dict.keys():
  
    a = []
    for z in user_dict[i]:
        if z in y:
            a.append(z)
        res[i] = a
 

print("Uncommon elements records : " + str(res))        
