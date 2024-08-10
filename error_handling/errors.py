# # anticipating errors / exceptions
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print("error")
# except NameError as e:
#     print("does not exist")
# else:
#     print("success")
# finally:
#     print("finally")
#
# # raising exceptions
# var_must_be_a_string = "test_string"
# if isinstance(var_must_be_a_string, str):
#     print(var_must_be_a_string)
# else:
#     raise TypeError(var_must_be_a_string)
#
# # stronger if
# a = 6
# assert a == 5

my_list = [1, 2, 3, 4, 5]
try:
    my_list[1]
except IndexError as e:
    print("IndexError")
else:
    print("index exists")
finally:
    print("finally")
