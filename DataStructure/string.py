
s1 = "Melu"
s2 = "Sahu"

print("Hello ")
print(s1)
print(s2)

# deleting a string
del s2;
print("After Deleting S2")
# print(s2)   # Will throw error


s1 = "Hii "
print(s1)


greet = "     Hi buddy, Good morning                  "

# replace(modify) string
greet = greet.replace("Hi", "Hey")
print(greet)

# access characters

print(greet[0])  # first character of the string
print(greet[-1])  # last character of the string


######### String Functions with example
print(len(greet)) # returns length of the string
print(greet.upper())  # returns upper case of the string
print(greet.lower())  # returns lower case of the string
print(greet.strip())  # remove void spaces (leading and trailing)
print(greet.replace("Hi", "Hey"))   # replace the existing string with updated word


## String Membership Testing

# 'in' keyword

print("Hi" in greet)
print("Hey" in greet)
print("morning" in greet)


#### repr and eval functions

# repr function is used to return a string representation of an object when passed to eval(). It mainly used for debugging, logging.

text = "Hello \n Buddy";
print(text)
print(repr(text))

stext = "sum([2, 3, 5])"
print(stext)
print(eval(stext))


# Convert string to a list in Python

li = greet.split()   # will convert each words in list
print(li)

list2 = list(greet)    # will convert each letters in list (even spaces also)
print(list2)