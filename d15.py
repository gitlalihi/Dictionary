#Python – Group Similar items to Dictionary Values List
list=[]
num=int(input("Enter your number of list"))
for i in range(num):
    ele1=input("Enter your is 1 st element:")
    ele2=input("Enter your 2nd element:")
    current_list=[ele1,ele2]
    list.append(current_list)
print("Your  original list is :",list)
unique_items=set(list)
res={key:[] for key in unique_items}
[res[item].append(item) for item in list]
print("Your similiar items to Dictionary Values List:",list)

