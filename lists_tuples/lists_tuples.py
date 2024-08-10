# my_list = ['apple', 'banana', 1, 2, 4]
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.append(14)
# print(my_list)
#
# my_tuple = ('apple', 'banana', 1, 2, 4, ['miles', 'mutuma'])
# print(my_tuple)
#
# print(my_tuple[1])
# print(my_list[1])
#
# # slicing
# test_list = [1, 2, 3, 4, 5]
# print(test_list[1:2])

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
negative_slicing = test_list[-1:4:-1]
default_slicing = test_list[::2]
print(default_slicing)
print(negative_slicing)

#excercise:
#start from 8 and go to 2, pick every secnd element
solution = test_list[7:0:-2]
print(solution)
