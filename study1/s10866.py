from collections import deque
import sys

n = int(sys.stdin.readline())
ans = []

dq = deque()

for i in range(n):
    sen = sys.stdin.readline().split()

    if sen[0] == "push_front":
        dq.appendleft(int(sen[1]))
    elif sen[0] == "push_back":
        dq.append(int(sen[1]))
    elif sen[0] == "pop_front":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq.popleft())
    elif sen[0] == "pop_back":
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq.pop())
    elif sen[0] == "size":
        ans.append(len(dq))
    elif sen[0] == "empty":
        if len(dq) == 0:
            ans.append(1)
        else:
            ans.append(0)
    elif sen[0] == "front":
        if len(dq) == 0:
            ans.append(-1)
        else:
            a = dq.popleft()
            ans.append(a)
            dq.appendleft(a)
    else:
        if len(dq) == 0:
            ans.append(-1)
        else:
            a = dq.pop()
            ans.append(a)
            dq.append(a)

for e in ans:
    print(e)