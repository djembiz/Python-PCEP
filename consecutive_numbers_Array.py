"""
Given an unsorted array of integer, find the longest sequence of consecutive numbers in the array
"""


def consecutive_arr(mylist: list):
    mylist.sort()
    #print(mylist)
    cons = [] # Temp array
    non_consecutive_found = None

    for i in range(len(mylist) -1):
        j = i + 1
        try:
            if (mylist[j] - mylist[i]) == 1:  # Consecutive Values
                if mylist[i] not in cons:  # Avoid duplicates
                    cons.append(mylist[i])
                cons.append(mylist[j])
            else:  # Non consecutive Values
                try:
                    if cons[i] == cons[i-1] + 1:  # current element and previous are consecutive
                        pass
                    else: # current and previous elements are not consecutive, remove current element
                        cons.pop(i)
                        non_consecutive_found = True
                except IndexError:
                    continue
        except IndexError:
            continue
    # Try again if nonconsecutive values were found earlier
    if non_consecutive_found:
        mylist.clear()
        mylist = cons[:]  # New array without non_consecutive values
        cons.clear() # Empty the temp array
        consecutive_arr(mylist)

    # Now we have "cons", an array containing on sub-arrays of consecutive elements
    # What is the longest sub-array of consecutive elements?
    print("\nList of consecitive numbers: ", cons)
    count1 = 1
    count2 = 0
    idx1 = idx2 = 0
    for i in range(len(cons) - 1):
        if cons[i+1] == cons[i] + 1:  # consecutive elements
            count1 = count1 + 1
            idx1 = i  # Elements at next index is consecutive to the current
        else:  # Non-consecutive elements
            if count1 >= count2:  # If there was a longer sub-array of consecutive elements
                count2 = count1  # save count of longest sub-array of consecutive elements so far
                count1 = 1  # Reinitialize consecutive the counter
                idx2 = i  # This is where the longest sub-array of consecutive numbers stopped - Excluded

    if count1 > count2:  # In case a more recent longer sub-array was found
         count2 = count1

    idx1 = 0
    for i in range(idx2, -1, -1):
        if cons[i] - cons[i-1] > 1:
            idx1 = i
            break

    print("The longest sequence of consecutive numbers is", count2," = ", cons[idx1:idx2+1])
    print()

# mylist = [4, 2, 1, 6, 5, 9, 4, 7, 5, 6,8, 10, 9, 15, 17, 20, 22]
# mylist = [4, 5, 6, 12, 13]


mylist = [1, 2, 4, 5 ,6 ,10, 8, 15, 12, 13,14,17,20,22,23,30, 31,32]
consecutive_arr(mylist)