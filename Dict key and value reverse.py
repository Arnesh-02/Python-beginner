def invert_dict(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict

# Sample Input
dict1 = {'Reg.No': 123, 'Name': 'abc', 'Course': 'CSE'}

# Invert the dictionary
inverted_dict1 = invert_dict(dict1)

# Print the inverted dictionary
print("Inverted Dict:", inverted_dict1)
