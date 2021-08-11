import sys
from types import TracebackType

n = int(sys.stdin.readline())
cnt = 0
num = 666

while(True):
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1

# import sys

# n = int(sys.stdin.readline())
# cnt = 0
# num = 0

# while(cnt != n):
#     string_num = str(num)
#     ans = 0
#     if string_num[-1] != '6':
#         ans = string_num + '6'*3
#         cnt += 1
#     else:
#         if len(string_num) >= 3 and string_num[-3:] == '666':
#             for i in range(1000):
#                 if i < 10:
#                     ans = string_num + '0'*2 + str(i)
#                 elif i < 100:
#                     ans = string_num + '0' + str(i)
#                 else:
#                     ans = string_num + str(i)
#                 cnt += 1
        
#         elif len(string_num) >= 2 and string_num[-2:] == '66':
#             for i in range(600, 700):
#                 ans = string_num + str(i)
#                 cnt += 1
        
#         else:
#             for i in range(660, 670):
#                 ans = string_num + str(i)
#                 cnt += 1
    
#     num += 1
#     if cnt == n:
#         print(int(ans))