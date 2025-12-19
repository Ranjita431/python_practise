# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict["model"])

# x = thisdict.get("year")
# print(x)

# a = thisdict.keys()
# print(a)

car = {
    "brand": "Toyota",  
    "model": "Corolla",
    "year": 2020
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
