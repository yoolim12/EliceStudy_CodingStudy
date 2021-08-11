###### 시간 초과 #######

# import sys
# import math

# def is_prime(n):
#     if n == 2:
#         return True
#     else:
#         for e in range(2, n):
#             if n % e == 0:
#                 return False
#             if e == n - 1:
#                 return True

# def main():
#     a, b = map(int, sys.stdin.readline().split())

#     cnt = 0
#     for num in range(a, b+1):
#         power = 2
#         for prime in range(2, b+1):
#             if is_prime(prime):
#                 while math.pow(prime, power) <= b:
#                     if math.pow(prime, power) >= a:
#                         cnt += 1
#                         power += 1
    
#     print(cnt)

# main()

import sys
import math

# def is_prime(n):
#     if n == 2:
#         return True
#     else:
#         for e in range(2, n):
#             if n % e == 0:
#                 return False
#             if e == n - 1:
#                 return True

def is_prime(n):
    if n == 2:
        return True
    else:
        prime_list = [elem for elem in range(3, n+1) if elem % 2 != 0]
        if prime_list[0] == n:
            return True
        else:
            for i in range(len(prime_list)):
                if prime_list[i] % prime_list[0] == 0:
                    del prime_list[i]


def main():
    a, b = map(int, sys.stdin.readline().split())

    cnt = 0
    sqrt_b = int(math.sqrt(b))

    for e in range(2, sqrt_b + 1):
        if is_prime(e):
            power = 2
            while math.pow(e,power) <= b:
                if math.pow(e,power) >= a:
                    cnt += 1
                power += 1
    
    print(cnt)

main()