def my_function(*args):
    print("Type",type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("Third argument:", args[2])
    print("All arguments:", args)
    my_function("apple", "banana", "cherry")
