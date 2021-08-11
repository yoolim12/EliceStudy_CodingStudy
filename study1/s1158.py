#deque-> rotate(-1), .join
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = [i for i in range(1, n+1)]
res = []

for num in range(n):
    for del_num in range(1, k+1):
        pop_elem = q.pop(0)
        if del_num != k:
            q.append(pop_elem)
        else:
            res.append(pop_elem)

print("<", end='')
for e in res:
    if e != res[-1]:
        print("%s, " %(e), end='')
    else:
        print("%s" %(e), end='')
print(">")


# from queue import Queue

# n, k = map(int, input().split())
# q = Queue()

# result = []

# for queue_elem in range(1, n+1):
#     q.put(queue_elem)

# for num in range(n):
#     for del_num in range(1, k+1):
#         pop_elem = q.get()
#         if del_num != k:
#             q.put(pop_elem)
#         else:
#             result.append(pop_elem)

# print(result)