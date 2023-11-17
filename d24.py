#Counting the frequencies in a list using dictionary in Python
def CountFrequency(my_list):
 
    
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print("% d : % d" % (key, value))
 
if __name__ == "__main__":
    my_list = []
    num=int(input("Enter your list:"))
    for i in range(num):
        ele=input("Enter your elements:")
        my_list.append(ele)
    print(" Your List:",my_list )   
    CountFrequency(my_list)