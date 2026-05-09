
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




# --------------The Memory Trap (Shallow Copy and Deep Copy) ---------------

original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = original.copy()

# If we change a top-level element, it's fine:
shallow_copy.append([7, 8, 9]) 
# original remains [[1, 2, 3], [4, 5, 6]] (Good!)
print("Original : ", original)
print("Shallow Copy : ", shallow_copy)

# BUT... if we change a NESTED element:
shallow_copy[0][0] = "TRAP"

print(original[0]) 
# Output: ["TRAP", 2, 3]  <-- IT CHANGED THE ORIGINAL TOO!


# Why did this happen?
# Even though shallow_copy is a new list at a new address, shallow_copy[0] still contains the exact same memory address as original[0]. They are both pointing at the same "inner" list.


# The Solution: Deep Copy
# If you want a truly independent version where nothing is shared, you must use a Deep Copy. This recursively wanders through the list and creates brand-new copies of every object it finds.



# -------------------------------------- Shallow Copy & Deep Copy -------------------------------------
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original)

deep_copy[0][0] = "SAFE"

print(original[0]) 
# Output: [1, 2, 3] (The original is untouched!)

# --------------Summary Rule of Thumb:
# Simple list (integers, strings, floats): Shallow copy is plenty.
# Nested list (lists inside lists, dicts inside lists): Deep copy is the only way to be safe.


# ------------------------------------------- Big O performance Example ------------------------------

import time

# Scenario A: Appending to the END (O(1))
start = time.time()
end_list = []
for i in range(100000):
    end_list.append(i)
print(f"Append to end: {time.time() - start:.4f} seconds")

# Scenario B: Inserting at the FRONT (O(n))
start = time.time()
front_list = []
for i in range(100000):
    front_list.insert(0, i)
print(f"Insert at front: {time.time() - start:.4f} seconds")
