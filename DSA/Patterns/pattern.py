

class PatternSolution :

    def pattern1(self, n):
        for i in range (1, n):
            print("*"*n)

    def Pattern2(self, n):
        for i in range(1, n):
            print("*"*i)
    
    def Pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end='')
            print()
    
    def Pattern4(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end='')
            print()
    
    def Pattern5(self, n):
        for i in range(0, n):
            for j in range(1, (n-i)+1):
                print("*", end='')
            print()

    def pattern6(self, n):
        for i in range (0, n):
            for j in range(1, (n-i+1)):
                print(j, end='')
            print()

    def pattern7(self, n):
        for i in range (1, n+1):
            for j in range(0, (n-i+1)):
                print(i, end='')
            print()


    def pattern8(self, n):
        for i in range (1, n):
            for j in range(0, (n-i+1)):
                print(" ", end='')
            
            for k in range(0, (2*i-1)):
                print("*", end='')

            for l in range(0, (n-i+1)):
                print(" ", end='')
            print()
            
    
    def pattern9(self, n):
        for i in range (1, n+1):

            for j in range(1, i):
                print(" ", end='')
            
            for k in range(0, (2*(n -i) +1)):
                print("*", end='')

            for l in range(1, i):
                print(" ", end='')
            print()

    def pattern10(self, n):
        for i in range (1, n+1):
            for j in range(0, (n-i+1)):
                print(" ", end='')
            
            for k in range(0, (2*i-1)):
                print("*", end='')

            for l in range(0, (n-i+1)):
                print(" ", end='')
            # print()

            for j in range(1, i):
                print(" ", end='')
            
            for k in range(0, (2*(n -i) +1)):
                print("*", end='')

            for l in range(1, i):
                print(" ", end='')
            print()

    def pattern11(self, n):
        for i in range (1, n):
            for j in range(1, (n-i+1)):
                print(" ", end='')
            
            for k in range(0, (2*i-1)):
                print("*", end='')

            for l in range(1, (n-i+1)):
                print(" ", end='')  
            print()

        for i in range (1, n+1):
            for j in range(1, i):
                print(" ", end='')
            
            for k in range(0, (2*(n -i) +1)):
                print("*", end='')

            for l in range(0, i):
                print(" ", end='')
            print()

    def pattern12(self, n):
        for i in range(1, 2*n-1):
            stars = i
            if(i>n): stars =  2*n-i

            for j in range(1, stars):
                print("*", end='')
            print()
    
    def pattern13(self, n):
        for i in range(1, n):
            for j in range(1, i+1):
                print(j, end='')
            for j in range(0, 2*(n-i-1)):
                print("*", end='')
            for j in range(i, 0, -1):
                print(j, end='')
            print()
    
    def pattern14(self, n):
        num = 1
        for i in range(1, n+1):
            for j in range(0, i):
                print(num, end='')
                num = num+1
            print()



pattern = PatternSolution()


# pattern.pattern1(5)
# pattern.Pattern2(5);

# pattern.Pattern3(5)
# pattern.Pattern4(5)
# pattern.Pattern5(5)
# pattern.pattern6(5)
# pattern.pattern7(5)
# pattern.pattern8(5)
# pattern.pattern9(5)
# pattern.pattern10(5)
# pattern.pattern11(5)
# pattern.pattern12(5)
# pattern.pattern13(5)
pattern.pattern14(5)
