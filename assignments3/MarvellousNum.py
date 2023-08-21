import math
def chkPrime(num):
    for i in range(2,math.ceil(num/2)):
        if num % i == 0:
            return False
    return True