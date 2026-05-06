
# List In Python 

# creating list
a = [1, 2,3,4,5,6]  #list of integers
b = ['apple', 'banana', 'mango'] # list of strings
c = [1, 'cherry', 12.05, True] # Hetrogeneous List (Mixed Data Types)

# creating list using list custructor

li = list((1, "Hii", 12.5, False))
name = list("Melu")
print(a)
print(b)
print(c)
print(li)
print(name)

a = [2]*3
print(a)


# Accessing List Elements

print(b[0])
print(b[1])
print(b[-1])
print(b[0:2])


# #############  Adding Elements into List

b.append("cherry")  # append cherry at last index
print(b)

b.insert(2, "Pineapple")  # add in 3rd place (2  index)
print(b)

b.extend(["Greps", "Water Mellon", "Kiwi"])  # add multiple items at once in last index
print(b)



########## Removing Elements from list

b.remove("banana")   # will remove the banana from the list
print(b)

popped_val = b.pop(1) # will remove the element from list present at 1 index and will return the value of that
print(popped_val)
print(b)

del b[0]   # will delete the 0th element of the list
print(b)

# b.clear()  # will remove all the elements from the list
# print(b)

######################### Iterating over the list

for fruit in b:
    print(fruit)


###################### List Comprehension

squares = [x**2 for x in range(1,6)]
print(squares)





########### Importent Insite
list1 = [1, 2]
list2 = [1, 2]

# Check if list objects are the same
lists_same = list1 is list2

# Check if the integers inside are the same objects
el1_same = list1[0] is list2[0]
el2_same = list1[1] is list2[1]

print(f"{lists_same=}")
print(f"{el1_same=}")
print(f"{el2_same=}")
print(f"Address of 1: {id(list1[0])}")
print(f"Address of 1: {id(list2[0])}")


# -------------Summary of your logic-----------------

# The Lists: Different memory addresses (Unique containers).
# The Elements: Same memory addresses (Shared pointers).
# Mutation: If you change an element, that specific list just gets a new pointer to a new object.