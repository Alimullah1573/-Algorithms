#   G.C.D   :   Greatest Common Divisor



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
