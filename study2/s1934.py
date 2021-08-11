"""
import sys
lcm = []

def gcd(a, b):
    if b == 0:
        return a
    else:"""
        # gcd(b, a % b) <<-- 이걸 return 없이 그냥 이렇게 쓰면 None을 return 한다. 왜일까?

"""
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
"""
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

