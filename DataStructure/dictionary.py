

# Discionary is a data structure that stores key-value pairs. While keys must be unique and immutable, values can be mutable or immutable.


dic = {"name":"Melu", "age": 25}
dicb = dict(name="Melu", age=25)


print(dic)
print(dicb)

print(f"Name is {dic['name']}")
print(f"Age is {dic.get('age')}")


# Note: Accessing a missing key with [ ] raises a KeyError, while get() is safer because it returns None (or a default value) instead of an error.

dic['gender'] = 'male'
print(dic)

dic['age'] = 26
print(dic)

del dic["age"]
print(dic)