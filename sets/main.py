my_set = {1, 2, 3, 4}
print(my_set)
my_set.add(6)
my_set.remove(4)
print(my_set)
print(list(my_set)[0])

# Comparason operators
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

#get items not in set 2
print(set1.difference(set2))