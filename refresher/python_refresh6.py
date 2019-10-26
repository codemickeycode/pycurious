# Dictionaries
# - dictionaries are a way store store information
#   in a key-value way
#   compared to a list just having things in order
# - there's no order to dictionaries
#
# - example: I want to look up this specific value with this specific key
#
# - create a dictionary
# - deleting items from a dictionary
# - adding items to a dictionary
# - updating the value of an item in a dictionary
#
# - items in a dictionary don't have to be of the same type

dogs = {"Fido":8, "Sally":17, "Nimeria":2}

print(dogs)
# print(dogs[2])
print(dogs["Sally"])

# del(dogs["Fido"])

del dogs["Fido"]

print(dogs)

dogs["Sarah"] = 6

# print(dogs)

dogs["Mickey"] = 3

print(dogs)

dogs["Sarah"] = False

print(type(dogs["Sarah"]))
print(dogs)


print(isinstance(dogs["Sarah"], (bool)))