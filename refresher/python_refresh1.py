# Variables, Strings, Ints and Prints
# - Declaring variables
# - How to make variables, ints
# - How to do strings
# - How to do prints
# - How to do some string concatenation

age = 33
name = """
Mickey
Mouse
Hello {}
""".format("World")

count = 1
count2 = 2

samplestring = "Mickey" + str(count) + " Mouse"
samplestring2 = "Mickey {} {} Mouse".format(count, count2)

print(name)

print(samplestring)
print(samplestring2)

# print(age)
# print("Hello my name is Mickey and I am 33 years old")
# print("Hello my name is {} and I am {} years old".format(name, age))
