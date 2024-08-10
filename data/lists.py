# inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers"]
# inventory_numbers = [43, 12, 98, 421, 23, 4678]
#
# for name, number in zip(inventory_names, inventory_numbers):
#     print(name)
#     print(number)
#
# for index, name in enumerate(inventory_names):
#     print(f'{index}: {name}')

# list comprehension
my_list = []
for num in range(0, 100):
    my_list.append(num)

my_list_comp = [num if num < 20 else 0 for num in range(0, 100)]
# print(my_list_comp)

combined_comp = [[(x, y) for x in range(5)] for y in range(10)]
# for row in combined_comp:
#     print(row)

chess_board = [[f'{letter}{num}' for num in range(1, 9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
    print(row)
# print(chess_board)
