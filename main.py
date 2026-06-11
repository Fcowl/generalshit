import fnmatch
import math

mask = '34?8*9'

def get_divs(n):
    divs = []
    for d in range(2, math.isqrt(n)+1):
        if n % d ==0 :
            divs.append(d)
            divs.append(n // d)
    return divs
def is_prime(n):
    for d in range(2, math.isqrt(n)+1):
        if n % d == 0:
            return False
    return True




for i in range(0,10**7):
    if fnmatch.fnmatch(str(i),mask):
        divs = get_divs(i)
        c = 0
        for d in divs:
            if c>4:
                print(i)
                break
            if is_prime(d):
                c+=1
