# def my_function(*kids):
#     print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")


 def my_function(*args): not working
     print("Type",type(args))
     print("First argument:", args[0])
     print("Second argument:", args[1])
     print("Third argument:", args[2])
     print("All arguments:", args)

  my_function("apple", "banana", "cherry")

 def my_function(greeting , *args):
     print(greeting)
     for arg in args:
         print(arg)
 my_function("Hello!" , "apple" , "banana" , "cherry")


def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 2, 3))          # Output: 6
print(my_function(10, 20, 30, 40))   # Output: 100
print(my_function(5, 15))    
# Output: 20
print(my_function(6,17))
