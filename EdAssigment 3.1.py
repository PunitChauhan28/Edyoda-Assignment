# Write a Python function to sum all the numbers in a list.

def sum_list(l):
    total=0
    for val in l:
        total = total+val
    return total
my_list=[8,2,0,7,3]
print("sum of list is", sum_list(
