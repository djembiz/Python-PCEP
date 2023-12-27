"""
Given an array of integers and a value, determine if there are any integers in the array whose sum equals the given value
"""


def sum_2_eq_value(my_array: list, value: int):
    lst = []
    for i in range(len(my_array) - 1):
        for j in range(i+1, len(my_array), 1):
            if my_array[i] + my_array[j] == value:
                lst.append((my_array[i], my_array[j]))
    if len(lst) > 0:
        for x in lst:
            print("SUM" + str(x) + " = ", value)
    else:
        print("There are no -Two numbers- found, whose sum equals ", value)


#my_array = [1, 2, 4, 5 ,6 ,10, 8, 15, 12, 13,14,17,20,22,23,30, 31,32]
my_array = [1, 2, 4, 5 ,6 ,10, 8, 15, 12]
print(len(my_array))
value = int(input("Enter a value: "))
sum_2_eq_value(my_array, value)
