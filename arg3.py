
def my_function(greeting , *args):
    print(greeting)
    for arg in args:
        print(arg)
my_function("Hello!" , "apple" , "banana" , "cherry")
