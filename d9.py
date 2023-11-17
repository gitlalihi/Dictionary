#Python – Insertion at the beginning in OrderedDict
import collections 
d1=collections.OrderedDict()
while True:
    key=input("Enter your Key:")
    if not key :
        break
    value=input(f"Enter your value for key{key}:")
    d1[key]=value
print(" Your  First Ordered dictionary is :",d1)
  
d2=collections.OrderedDict()
while True:
    key=input("Enter your Key:")
    if not key :
        break
    value=input(f"Enter your value for key{key}:")
    d2[key]=value
print(" Your  Second  Ordered dictionary is :",d2)
o_dict = list(d1.items()) + list(d2.items())
 

print ("Resultant Dictionary :"+str(o_dict))
  
