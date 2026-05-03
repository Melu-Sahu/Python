

#### Conditional Statements

a = 5
b = 5
if(a > b):
    print(f"{a} is greater then {b}")
elif(a==b):
    print(f"{a} is equal to {b}")
else: 
    print(f"{a} is less the {b}")




c = a>b   # contails True or False

print(c)

if(c):
    print("True")
else: 
    print("False")



if(c and a<b):
    print("Logical AND True")
else: 
    print("Logical AND False")

if(c or a<b):
    print("Logical OR True")
else : 
    print("Logical OR False")


if not(a<b):
    print("Logical NOT True")
else : 
    print("Logical NOT False")



####### Like Turnery Operator , below is short form of if else statement

age = 19

if age > 18 : print("Eligable for voting.")



marks = 80

result = "pass" if marks >= 33 else "fail"
print(f"Result is : {result}")
############### Match Case

p = 7

match p :
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Default Case.")