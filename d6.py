#Ways to sort list of dictionaries by values in Python
num_dicts = int(input("Enter the number of dictionaries: "))

list_of_dicts = []

for _ in range(num_dicts):
    item = input("Enter item: ")
    value = int(input("Enter value: "))
    data = {'item': item, 'value': value}
    list_of_dicts.append(data)


print("List of dictionaries:", list_of_dicts)
def sort_by_age_and_score(item):
    return item['value']
sorted_list = sorted(list_of_dicts, key=sort_by_age_and_score)
print(sorted_list)