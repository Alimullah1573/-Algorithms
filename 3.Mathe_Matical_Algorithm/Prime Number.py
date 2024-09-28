
import  math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input())
    if is_prime(num):
        print(f"{num} it is a Prime Number")
    else:
        print("It is not a prime number")
