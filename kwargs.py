# def my_funtion(**myvar):
#   print("Typre:", type(myvar))
#   print("First name:", myvar["fname"])
#   print("Last name:", myvar["lname"])
#   print("Age:", myvar["age"])

#   my_funtion(fname="John" , lname="Doe" , age=30)
    

# def my_function(username, **details):
#   print("Username:", username)
#   print("Additional details:")
#   for key, value in details.items():
#     print(" ", key + ":", value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")