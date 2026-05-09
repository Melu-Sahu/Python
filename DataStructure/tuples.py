

# Creating a tuple
tup = ()
print(tup)

# Using String
tup = ('Melu', 'Sahu')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Melu')
print(tup)

# Tuple with Mixed Data Types
tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)



not_a_tup = (5)   # This is just a integer 5
is_a_tup = (5,)   # This is a tuple

name = ("Melu")
name_tup = ("Melu",)
print(not_a_tup)
print(is_a_tup)
print(name)
print(name_tup)



############# Deep Copy and Shallow Copy with Tuples

my_tup = (1, 2, ["a", "b"])
print(my_tup)

print(my_tup[0])
# my_tup[0] = 100   # will throw error because of it's immutability
my_tup[2].append("c")  # this will work because list inside it is mutable
print(my_tup)
# Reason : The tuple is only storing the memory address of the list. That address never changed: only the data at the address did.


print(tup.count(5))       # returns the occurance of 5 in tuple
print(tup.index('Welcome')) # returns then index of "Welcome" in tuple