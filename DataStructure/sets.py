

set1 = {1, 2, 3, 4}
set2 = set([1,2,3])

print(set1)
print(set2)

A = {1, 2, 3}
B = {3, 4, 5}

A.add(6)
print(A)

B.remove(5)
print(B)

print(A|B) # union
print(A&B) # intersection
print(A-B) # difference
print(B-A) # difference

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

C = {"Hello", 12.05, 2000, True}

print(C)

# D = {"Hello", [1, 2]}   # this like will throw error because list inside set breaks the hashabililty of sets. List is mutable

E = frozenset([1, 2, 4])
print(E)
# E.add(1)  # will throw error because in frozen set we cannot perform any add or remove actions




#------------------------------------ Remove Duplicate Elements -----------------------------


# If you want to remove duplicates and preserve the original order, use this dictionary trick:

items = ["apple", "banana", "apple", "cherry", "banana"]

# Dict keys must be unique. Since Python 3.7, dicts preserve insertion order!
clean_items = list(dict.fromkeys(items))

print(clean_items)  # Output: ['apple', 'banana', 'cherry']


# ------------------  Fastest Subset and Supeset checking --------------------------

required_skills = {"Python", "SQL", "Git"}
candidate_a = {"Python", "SQL", "Git", "Docker"}
candidate_b = {"Python", "HTML"}

# 1. Is Candidate A qualified? (Is required_skills a subset of candidate_a?)
print(required_skills.issubset(candidate_a))  # Output: True

# 2. Does candidate_b lack skills?
print(required_skills.issuperset(candidate_b))  # Output: False

# 3. Do they have absolutely NOTHING in common?
print(candidate_a.isdisjoint({"Java", "C++"}))  # Output: True


# ------------------ Modifying a set during comparision ------------------
active_users = {"Alice", "Bob", "Charlie"}
banned_users = {"Bob"}

# This modifies 'active_users' in place instead of creating a new set
active_users.difference_update(banned_users)

print(active_users)  # Output: {'Alice', 'Charlie'}




