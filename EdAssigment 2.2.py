# Write a Python program to print a dictionary whose keys should be the alphabet
#  from a-z and the value should be corresponding ASCII values
ascii_dict = dict()
alfapet_Teller = range(97,123)
for i in alfapet_Teller:
    ascii_dict[str(i)] = chr(i)
print(ascii_dict)
