def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 2, 3))          # Output: 6
print(my_function(10, 20, 30, 40))   # Output: 100
print(my_function(5, 15))            # Output: 20