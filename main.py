import math
def find_divisors(n:int) -> set[int]:
    divisors = set()
    for i in range(2, math.isqrt(n)+1):
        if len(divisors) > 3:
            return set()
        if n % i == 0:
            divisors.update({i, n // i})
    return divisors


for i in range(106_732_567, 152_673_836):
    divs = find_divisors(i)
    if len(divs) == 3:
        print(i,sorted(divs)[-1])

