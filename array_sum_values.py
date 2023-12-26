"""
Given an array of integers and a value, determine if there are any two integers in the array whose sum equals the given value
"""


def sum_2_eq_value(my_array: list, value: int):
    for i in range(len(my_array) -1):
        for j in range(i+1, len(my_array), 1):
            if my_array[i] + my_array[j] == value:
                print("SUM", (my_array[i], my_array[j])," = ", value)
                break
    else:
        print("There are no - Two numbers - whose sum equals ", value)


def sum_any_eq_value(my_array: list, value: int):
        sum = 0
        sum_list =[]
        for i in range(0, len(my_array) - 1, 1):
            if my_array[i] != 0:
                for j in range(i + 1, len(my_array), 1):
                    print(i, j)
                    sum_list.append(my_array[j])
                    sum = sum + my_array[i] + my_array[j]
                    if sum == value:
                        print(sum_list, value )
                        break
        else:
            print("There are no numbers - whose sum equals ", value)


my_array = [1, 2, 4, 5 ,6 ,10, 8, 15, 12, 13,14,17,20,22,23,30, 31,32]
print(len(my_array))
value = int(input("Enter a value: "))
#sum_2_eq_value(my_array, value)
sum_any_eq_value(my_array, value)