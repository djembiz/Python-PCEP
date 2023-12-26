def median_func(mylist: list):
    mylist = sorted(mylist)
    lgt = len(mylist)
    print(mylist)
    if lgt % 2 == 0:
        idx = lgt // 2
        med = (float(mylist[idx - 1]) + float(mylist[idx])) / 2
        return med
    else:
        idx = (lgt - 1) // 2
        return float(mylist[idx])


def array():
    array_lst = input("Enter elements, separated by spaces (Numeric values only): ")
    return array_lst.split(" ")


array_list1 = array()
array_list2 = array()
mylist = array_list1 + array_list2
for x in range(len(mylist)):
    mylist[x] = float(mylist[x])

print(median_func(mylist))







