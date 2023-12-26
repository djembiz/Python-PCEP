"""
Given a list of items with properties Weight/Value and a Max weight
find the maximum value we can generate from items where the sum of the
weights do not exceed the Max Weight

items = {(w:1,v:6),(w:2,v:10),(w:3,v:12)}
3 combination maximum
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


def knapsack(items: list, max_weight: int):
    #max_weight = int(input("What is the Max Weight?: "))
    value_max = 0
    for i in range(len(item_list)):
        for j in range(len(item_list)-1, i, -1):
            if item_list[i].weight + item_list[j].weight <= max_weight:
                max_value = item_list[i].value + item_list[j].value
                print(mylist[i], "and", mylist[j], "==>", max_value)
                if max_value >= value_max: value_max = max_value
                x = j - 1
                while x > i:
                    if item_list[i].weight + item_list[j].weight + item_list[x].weight <= max_weight:
                        max_value = max_value + item_list[x].value
                        print(mylist[i], "and", mylist[j], "and", mylist[x], "==>", max_value)
                        if max_value >= value_max: value_max = max_value
                    x -= 1
    print("Max Value: ", value_max)


nbr = int(input("How many items do we have?: "))
item_list = []
for i in range(nbr):
    item = create_item()
    item.num = i + 1
    item_list.append(item)  # list of items

# Display Items
mylist = []
for item in item_list:
    mylist.append((item.weight, item.value))
print(mylist)
#
max_weight = int(input("What is the Max Weight?: "))
knapsack(mylist, max_weight)




