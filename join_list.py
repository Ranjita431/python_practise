list1 = ["a", "b", "c"]
list2 = ["1", "2", "3"]

# listed = list1 + list2
# print(listed)

# for x in list2:
#     list1.append(x)
# print(list1)
list1.extend(list2)
print(list1)