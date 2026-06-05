

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


solution = Patterns();

# solution.pattern1(5); # time complexity O(n)
# solution.pattern2(5); # time complexity O(n)
# solution.pattern3(5); # time complexity O(n^2)
# solution.pattern4(5); # time complexity O(n^2)
# solution.pattern5(5); # time complexity O(n^2)
solution.pattern6(5); # time complexity O(n^2)
