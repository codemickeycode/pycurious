# Functions
# - how to create a function
# - give the function parameters
# - default values for the parameters
# - how to return information back from a function

# age = 12
# name = "Matt"
# today_is_code = True


# def hello():
#     print("Hello World")
#     print("Hello Isaac")
#     print("Hello Primary")

# hello()
# hello()
# hello()


# add parameters
# def hello(name, age):
#     print("Hello {} you are {} years old".format(name, age))

# hello("Mark", 20)
# hello(20, "Mark")


# # default values
# def hello(name="Isaac", age=0):
#     print("Hello {} you are {} years old".format(name, age))

# hello()


# return
def hello(name="Isaac", age=0):
    return "Hello {} you are {} years old".format(name, age)

sentence = hello(name="Oscar")
print(sentence)