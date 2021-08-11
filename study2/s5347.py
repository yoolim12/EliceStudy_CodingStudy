import sys
lcm = []

def gcd(a, b): # a > b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    _min = min(a, b)
    _max = max(a, b)
    _gcd = gcd(_max, _min)
    _lcm = int((a / _gcd) * b)
    lcm.append(_lcm)

for e in lcm:
    print(e)