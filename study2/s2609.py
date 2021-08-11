"""
< 유클리드 호제법 >
두 수 a와 b가 있을 때(a > b), a와 b의 최대공약수는 b와 a%b의 최대공약수와 같다.
"""

# import sys

# n1, n2 = map(int, sys.stdin.readline().split())

# div = 1
# mul = 1

# for i in range(1, max(n1, n2) + 1):
#     if n1 % i == 0 and n2 % i == 0:
#         div = i

# mul = int((n1 / div) * n2)

# print(div)
# print(mul)

"""import sys

n1, n2 = map(int, sys.stdin.readline().split())

div = 0
mul = 1

for i in range(min(n1,n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        div = i
        break

mul = int((n1 / div) * n2)

print(div)
print(mul)"""

import math
import sys

a, b = map(int, sys.stdin.readline().split())

print(math.gcd(a, b))
print(math.lcm(a, b))