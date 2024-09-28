#   G.C.D   :   Greatest Common Divisor

def GCD(num1, num2):
    while num2:
        # a, b swap and a % b val
        num1, num2 = num2, (num1 % num2)
    return num1

def LCM(num1, num2):
    return ((num1 * num2) // GCD(num1, num2))
# Driver Code
if __name__ == '__main__':
    # for _ in range(int(input().split()))
        num1, num2 = map(int, input().split())

        res_GCD = GCD(num1, num2)
        res_LCM = LCM(num1, num2)
        print(f'num1:->{num1} num2:->{num2}-> GCD:->',res_GCD)
        print(f'num1:->{num1} num2:->{num2}-> LCM:->', res_LCM)



# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 =  19
num2 = 17

print("The H.C.F. is", compute_hcf(num1, num2))




from math import gcd, lcm
a, b = 15, 20
print(f'{a} and {b}->GCD:->', gcd(a, b))
print(f'{a} and {b}->LCM:->', lcm(a, b))
