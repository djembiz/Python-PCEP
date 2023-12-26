"""
Given an array of integers, write a function to find all the duplicates in the array
"""


def create_array():
    mylist = input("Enter the elements of the array, Integers only, separated by spaces: ")
    mylist = mylist.split(" ")
    return mylist


def dupl(my_array: list):
    dup = []
    for i in range(len(my_array)):
        if my_array[i] in my_array[i+1:]:  # We want to consider all the element except the current element indexed
            if my_array[i] not in dup:
                dup.append(my_array[i])
        else:
            continue

    print("The list of duplicates: ", dup)


mylist = create_array()
print(mylist)
dupl(mylist)


