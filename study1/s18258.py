import sys
from collections import deque

dq = deque()

def push(x):
    dq.append(x)

def pop():
    if empty():
        return -1
    else:
        return dq.popleft()

def size():
    return len(dq)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def front():
    front = pop()
    if front != -1:
        dq.appendleft(front)
    return front

def back():
    if empty():
        return -1
    else:
        back = dq.pop()
        push(back)
        return back

def main():
    n = int(sys.stdin.readline())
    ans = []

    for i in range(n):
        sen = sys.stdin.readline().split()
        if sen[0] == "push":
            push(int(sen[1]))
        
        elif sen[0] == "pop":
            ans.append(pop())
        
        elif sen[0] == "size":
            ans.append(size())
        
        elif sen[0] == "empty":
            ans.append(empty())
        
        elif sen[0] == "front":
            ans.append(front())
        
        else:
            ans.append(back())
    
    for e in ans:
        print(e)

main()

##########시간 초과##########
# q = [] --> 리스트 말고 덱을 활용했더니 시간 초과가 되지 않았다.

# def push(x):
#     q.append(x)

# def pop():
#     if empty():
#         return -1
#     else:
#         f = q[0]
#         del(q[0])
#         return f

# def size():
#     return len(q)

# def empty():
#     if size() == 0:
#         return 1
#     else:
#         return 0

# def front():
#     if empty():
#         return -1
#     else:
#         return q[0]

# def back():
#     if empty():
#         return -1
#     else:
#         return q[-1]

# def main():
#     n = int(input()) --> input이 sys.stdin.readline 보다 더 시간 걸림
#     ans = []

#     for i in range(n):
#         sen = input()

#         if "push" in sen:
#             l = ""
#             for i in range(5, len(sen)):
#                 l += sen[i]
#             l = int(l)
#             push(l)
        
#         elif sen == "pop":
#             ans.append(pop())
        
#         elif sen == "size":
#             ans.append(size())
        
#         elif sen == "empty":
#             ans.append(empty())
        
#         elif sen == "front":
#             ans.append(front())
        
#         else:
#             ans.append(back())
    
#     for e in ans:
#         print(e)

# main()