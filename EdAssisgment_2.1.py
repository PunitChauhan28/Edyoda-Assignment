# Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

list1= []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele+1)  # adding the element
    print(list1)

