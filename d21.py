#Python | Remove all duplicates words from a given sentence
s1=input("Enter your String:")
print(' '.join(dict.fromkeys(s1.split())))