# fruits = ("apple", "banana", "cherry", "date")
# (a, b, c, d) = fruits
# print(a)
# print(b)
# print(c)

# fruits = ("apple", "banana", "cherry", "date", "fig", "grape")
# (green , yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

fruits = ("apple", "banana", "cherry", "date", "fig", "grape")
(green , *tropic, red) = fruits
print(green)
print(tropic)
print(red)