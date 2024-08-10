test_string = "this is a test"
test_list = [1, 2, 3, 4]

print(test_string.split("t"))
print(list(test_string))
print(tuple(test_string))

print(" ".join(["one, two", "three", "four"]))
# print(str(test_list))
exercise = (str(test_list).strip("[").strip("]")
            .replace(",",""))
print(exercise)