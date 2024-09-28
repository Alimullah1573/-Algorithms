
def factorial(Number):
    Result = 1
    for i in range(1,Number+1):
        Result *=i
    print(f"Number: {Number} , Result = {Result}")
if __name__ == '__main__':
    Number = int(input())
    factorial(Number)

# Recursion *****>>>>>
def Factorial(N):
    if N <= 1:
        return 1
    else:
        return N*Factorial(N-1)
if __name__ == '__main__':
    N = int(input())
    print(Factorial(N))



import math
n = int(input())
print(math.factorial(n))

