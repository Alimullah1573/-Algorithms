
# L.C.M = least Common Multiple
# GCD = Greatest Common Divisor




a = int(input('Enter a : '))
b = int(input('Enter b : '))
m = None
if a>b:
    m = a
else: m = b
"""for i in range(m,a*b+1,m):
    #print(i)
    if i%a == 0 and i%b == 0:
        print(f'LCM of {a},{b} is {i}')
        break"""
i = m
while i<=a*b:
        #print(i)
        if i % a == 0 and i % b == 0:
            print(f'LCM of {a},{b} is {i}')
            break
        i +=m


# Multiple Number's LCM

import  math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# Input list of numbers
numbers = [10, 11, 15, 20]  # You can replace this with any list of numbers

# Compute LCM
result = lcm_multiple(numbers)

print(f"LCM of {numbers} is {result}")