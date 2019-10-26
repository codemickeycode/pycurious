# Classes
# - creating a class in Python
# - adding methods (functions inside of class)
# - creating class properties
# - creating class variables
# - adding parameters to class methods
# - creating __init__ methods


class Dog:

    # this is going to be a class variable that can be accessed anywhere
    # it's not tied to a specific instance
    dog_info = "Hey dogs are cool"

    def bark(self, str):
        print("BARK! " + str)


# mydog = Dog()
# mydog.bark("Nimeria")
# mydog.name = "Fido"
# mydog.age = 16

# print(mydog.name)
# print(mydog.age)

# print(Dog.dog_info)
# Dog.dog_info = "Hey there"
# print(Dog.dog_info)


# class Dog:

#     def __init__(self, name="", age=0, furcolor=""):
#         self.name = name
#         self.age = age
#         self.furcolor = furcolor

#     def bark(self, str):
#         print("BARK! " + str)


# mydog = Dog("Fido", 13, "Brown")
# print(mydog)
# print(mydog.age)
# mydog.bark("Tokwa")

mydog = Dog()
# print(mydog.age)


mydog.bark = 1
print(mydog.bark)
mydog.bark("Tokwa")