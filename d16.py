#K’th Non-repeating Character in Python using List Comprehension and OrderedDict
from collections import OrderedDict
def repeat(input,k):
    dict=OrderedDict.fromkeys(input,0)
    for i in input:
        dict[i]=dict[i]+1
    extractkeys=[key for key ,value in dict.items() if value==1]
    if(len(extractkeys))<k:
        return'k than less non-repeating charachters'
    else:
        return extractkeys[k-1]
if __name__ == "__main__":
    input = "Helloworld"
    k = 2
    print (repeat(input, k))

