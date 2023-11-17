#Python Dictionary to find mirror characters in a string
s1=input("Enter your string:")
def find_mirror_chars(s1):
    mirror_dict={'a': 'a', 'b': 'd', 'c': 'c', 'd': 'b', 'e': 'e', 'f': 'f', 'g': 'g',
                   'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
                   'o': 'o', 'p': 'q', 'q': 'p', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
                   'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    mirrored_chars=[]
    for i in s1:
        if i.lower() in mirror_dict:
            mirrored_chars.append(mirror_dict[i.lower()])
        else:
            mirror_dict.append(i)
    mirrored_str=''.join(mirrored_chars)
    return mirrored_str

print("Your dictionary to find mirror charachters is :",find_mirror_chars(s1))