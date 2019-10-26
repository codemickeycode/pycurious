# Lists
# Python calls them lists instead of arrays
# - lists are ordered
# - creating a list
# - inserting items on a list
# - deleting items from a list
# - updating the value of an item in a list
# - items in a list don't have to be of the same type

dognames = ["Mark", "Patras", "Lady", "Nimeria"]

dognames.insert(0, "Jane")

print(dognames)
print(dognames[2])

del dognames[2]
print(dognames)

dognames[1] = "Mark new"
print(dognames)
print(len(dognames))

# print(dognames)


dognames = ["Mark", "Patras", "Lady", "Nimeria", 234, False, True, 1.2345, {}]

print(dognames)