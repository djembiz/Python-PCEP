"""
Given a list of items with properties Weight/Value and a Max weight
find the maximum value we can generate from items where the sum of the
weights do not exceed the Max Weight

items = {(w:1,v:6),(w:2,v:10),(w:3,v:12)}
maxWeight = 5
knapsack(items,maxWeight)=22
"""
"""
Djeme Doli 12/19/23
"""


class ITEM:
    def __int__(self, num: int,  weight: int, value: int):
        self.num = num
        self.weight = weight
        self.value = value


def create_item():
    item = ITEM()
    item.num = 0
    item.weight = int(input("Item weight: "))
    item.value = int(input("Item value: "))
    return item


nbr = int(input("How many items do we have?: " ))
item_list = []
for i in range(nbr):
    item = create_item()
    item.num = i + 1
    item_list.append(item) # list of items

# Display Items
mylist = []
for item in item_list:
    mylist.append((item.weight, item.value))
print(mylist)
#
maxWeight = int(input("What is the Max Weight?: "))
vals = []
j = len(item_list)
for i in range(len(item_list)):
    for j in range(len(item_list)-1, i, -1):
        #print(i, j)
        if item_list[i].weight + item_list[j].weight <= maxWeight:
            maxValue = item_list[i].value + item_list[j].value
            print(mylist[i], "and", mylist[j], "==>", maxValue)
            #vals.append(maxValue)




