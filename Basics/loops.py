

# Loops In Python 

# 1. For Loops
# 2. While Loop



####### For Loops

n = 5

for a in range(0, n):
    print(a)


for b in range(10):
    if(b >= 5): 
        continue  # skip the remaining operations of the loop
        # break   # break the loop
        # pass    # does nothing
    print(b)
    
names = ["Melu", "Tony", "Steve"]

for name in names:
    print(name)


for letter in 'melusahu':
    pass
print('Last Letter :', letter)




############# While Loop


count = 5

while(count <10):
    print(count)
    count = count+1

# Infinite loop beloe
# while (True):
#     print("Hello Buddy")


