import math
while True:
    try:
        m,n=[int(x) for x in input().split()]
        print(math.gcd(m,n))
    except EOFError:
        break