

# Function in Python 


# defination


def myFun():
    print("This is user defined function")


# def keyword stands for user defined function.

###### Arguements
## Keyword Arguement

def funOne(key1, key2):
    print("Example of Keyword Arguement")
    print(f"Key 1 : {key1}")
    print(f"Key 2 : {key2}")

funOne(1, "Hello")
# funOne("Hello") # will throw error


## Arbitrary Argument

# *arg are stored in tuples
# **kwarg are stored in dictionary (dict)

def funTwo(*arg, **kwarg):
    print("ARG's ARE : ", *arg)
    # print("KWARG's ARE : ", **kwarg)

funTwo("melu", "sahu", age = 26, role = "ssc")


############ Anonymous Funcitons


def square(x) : return x*x
multiply = lambda x, y : x*y


print(square(7))
print(multiply(4,5))

