a  = "Hello"
print(a)


# name = input("Enter your name ... : ")
# print ("Your Name is : " + name)

b = 5
print ("b is : ", b)


c = d = e = 5
print(f"C : {c}, D : {d}, E : {e}")

p = ["Hyd", "Mumbai", "Delhi"]

# a, b, c = p
# print(f"City 1 : {a}, city 2 : {b}, city 3 : {c}")


# Casting
c = float(c)
print(type(c))




######### Scope of the variable ##############

a = "global variable";

def myFun():
    a = "local variable"
    global x
    x  = "global inside function"
    print(a)
    print(x)

myFun()
print(a)


######  Data Types ##########

var1 = str("STring")
var2 = int(20) 
var3 = float(20.45)


####
/* 
    Text Type (Sring)   - str
    Numeric Type        - int, float, complex
    Sequence            - list, tuple, range
    Mapping Type        - dict
    Set Type            - Set, frozenset
    Boolean             - bool
    Binary              - bytes, bytearray, memoryview
    None                - none type
*/



