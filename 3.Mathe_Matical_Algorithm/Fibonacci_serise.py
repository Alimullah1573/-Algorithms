def Fibonacci(N):
    Fibonacci_list = [0,1]
    for i in range(N-2):
        Fibonacci_list.append(Fibonacci_list[-1] + Fibonacci_list[-2])
    return Fibonacci_list

if __name__ == '__main__':
    # Input Number
    N = int(input())
    serise = Fibonacci(N)
    # Fibonacci sirise
    print(f"Number({N}):",*serise,end=" ")

print()
# Recursion
def Fibonacci(Number):
    if Number <=1:
        return Number
    else:
        return Fibonacci(Number-1) + Fibonacci(Number-2)
if __name__ == '__main__':
    Number = int(input()) # User Input()
    for i in range(Number):

        print(Fibonacci(i),end=" ")






