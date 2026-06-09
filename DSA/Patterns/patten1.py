

class Patterns:
    def pattern1(self, n):
        for i in range (0, n):
            print("*"*n)
    
    def pattern2(self, n):
        for i in range(1, n+1):
            print("*"*i)

    def pattern3(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    def pattern4(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
                
    def pattern5(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end="")
            print('')
    
    def pattern6(self, n):
        for i in range(1, n):
            for j in range(1, (n-i+1)):
                print("*", end='')
            print('')

    def pattern7(self, n):
        for i in range(1, n):
            for j in range(0, n-i):
                print(" ", end='')
            for j in range(0, 2*i-1):
                print("*", end='')

            for j in range(0, n-i):
                print(" ", end='')
            print()
    
    def pattern8(self, n):
        for i in range(0, n):
            for j in range(0, n-i):
                print(" ", end='')
            for j in range(0, 2*i-1):
                print("*", end='')

            for j in range(0, n-i):
                print(" ", end='')
            print()
    
    def pattern9(self, n):
        for i in range(0, n):
            for j in range(0, i):
                print(" ", end='')
            for j in range(0, 2*(n-i)-1):
                print("*", end='')

            for j in range(0, i):
                print(" ", end='')
            print()
    def pattern10(self, n):
        for i in range(0, 2*n-1):
            stars = i
            # if(i>n): stars = 2*n-i

            if(i<n):
                print("*"*(i+1))
            else:
                print("*"*(2*n-i-1))
            # for j in range(0, stars):
            #     print("*", end='')
            # print()

    def pattern11(self, n):
        start = 1
        for i in range(0, n):
            if(i%2==0): 
                start = 1
            else:
                start = 0
            for j in range(0, i):
                print(start, end='')
                start = 1-start
            print()

    def pattern12(self, n):
        for i in range(1, n):
            for j in range(1, i):
                print(j, end='')
            for j in range(1, 2*n-i):
                print(" ", end='')
            for j in range(1, i):
                print(2*i -j, end='')
            print()

solution = Patterns();

# solution.pattern1(5); # time complexity O(n)
# solution.pattern2(5); # time complexity O(n)
# solution.pattern3(5); # time complexity O(n^2)
# solution.pattern4(5); # time complexity O(n^2)
# solution.pattern5(5); # time complexity O(n^2)
# solution.pattern6(5); # time complexity O(n^2)
# solution.pattern8(5); # time complexity O(n^3)
# solution.pattern9(5); # time complexity O(n^3)
# solution.pattern11(10); # time complexity O(n)
solution.pattern12(6); # time complexity O(n)
