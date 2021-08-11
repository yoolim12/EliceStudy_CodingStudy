"""
sum = 0
for i in range(1,6):
    sum += i
print(sum)

-->> 이런 경우엔 sum = 15로 나오는데,
아래와 같은 코드에서 m = 60, n = 100을 넣었을 때, 왜 _min과 sum 값이 변한 값이 아닌 초기값으로 나오는걸까...

--------------------------------------

import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

_min = 0
sum = 0
cnt = 0

for e in range(m, n+1):
    for less_than_e in range(1, e):
        if less_than_e == e - 1:
            cnt += 1
            sum += e
        elif e % less_than_e == 0:
            break
    if cnt == 1:
        _min = e

print(sum)
print(_min)
"""


# import sys

# def main():
#     _min = 0
#     sum = 0
#     cnt = 0
    
#     m = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())

#     for e in range(m, n+1):
#         for less_than_e in range(2, e):
#             if less_than_e == e - 1:
#                 cnt += 1
#                 sum += e
#             elif e % less_than_e == 0:
#                 break
#         if cnt == 1:
#             _min = e

#     if cnt == 0:
#         print(-1)
#     else:
#         print(sum)
#         print(_min)

# main()



"""
<그냥 실험>

def a():
    global b
    b = "ahhhhhhhh"
a() <<--- 이렇게 함수를 먼저 실행해줘야
print(b) <<-- b 를 "ahhhh"로 인식한다.
"""

# 얘도 잘 되는데........
# def a():
#     global sum
#     sum = 0
#     for i in range(1,6):
#         sum += i
# a()
# print(sum)

import sys

def is_prime(n):
    if n == 2:
        return True
    else:
        for e in range(2, n):
            if n % e == 0:
                return False
            if e == n - 1:
                return True

def main():
    cnt = 0
    sum = 0
    min = 0

    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    for e in range(m, n+1):
        if is_prime(e):
            cnt += 1
            sum += e
        if cnt == 1:
            min = e
            cnt = 100
    
    if cnt == 0:
        print(-1)
    else:
        print(sum)
        print(min)

main()