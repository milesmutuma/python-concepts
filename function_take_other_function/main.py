# list1 = [4, 2, 3, 1, 5]
#
# list1.sort()
# print(list1)

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]


def sort_fuc(item):
    return item[1]


# print(sorted(list2, key=sort_fuc))
print(sorted(list2, key=lambda item: item[1]))

inventory_names = ['Screws', 'Wheels', 'Metal Parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 4]
combined_list = list(zip(inventory_names, inventory_numbers))
print(sorted(combined_list, key=lambda item: item[1]))
print(sorted(combined_list, key=lambda item: len(item[0]), reverse=True))


# Map
def power_func(num):
    return num ** 2


print(list(map(lambda num: num ** 2, range(10))))


def get_below_4(num):
    return num < 4


print(list(filter(get_below_4, range(10))))

print(list(filter(lambda num: num < 4, range(10))))

# replace map with list comprehension
print([num for num in range(10) if num < 4])
