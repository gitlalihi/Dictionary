#Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
from collections import Counter

def make_string_by_deletion_and_rearrangement(str1, str2):
    
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    common_characters = list((counter1 & counter2).elements())
    common_character_freq = {char: min(counter1[char], counter2[char]) for char in common_characters}
    new_string = ''.join([char * freq for char, freq in common_character_freq.items()])

    return new_string

string1 = "Hello"
string2 = "egg"
result = make_string_by_deletion_and_rearrangement(string1, string2)
print(f"Original String 1: {string1}")
print(f"Original String 2: {string2}")
print(f"New String: {result}")
