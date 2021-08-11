# BFS
import sys
from collections import deque

def BFS(graph, root):
    visited = [root]
    queue = deque([root])

    while queue:
        cur = queue.popleft()

        for node in graph[cur]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    
    return visited

def main():
    computer_num = int(sys.stdin.readline())
    computer_linked = int(sys.stdin.readline())
    computer_graph = {i:[] for i in range(1,computer_num+1)}

    for n in range(computer_linked):
        n1, n2 = map(int, sys.stdin.readline().split())
        computer_graph[n1].append(n2)
        computer_graph[n2].append(n1)
    
    search = BFS(computer_graph, 1)
    print(len(search) - 1)

main()

######## 이렇게 하면 for문에서 오류가 난다. --> 위에 처럼 양방향 그래프로 바꿔준다!! ########
# # BFS
# import sys
# from collections import deque

# def BFS(graph, root):
#     visited = [root]
#     queue = deque([root])

#     while queue:
#         cur = queue.popleft()

#         for node in graph[cur]:
#             if node not in visited:
#                 visited.append(node)
#                 queue.append(node)
    
#     return visited

# def main():
#     computer_num = int(sys.stdin.readline())
#     computer_linked = int(sys.stdin.readline())
#     computer_graph = {}

#     for n in range(computer_linked):
#         n1, n2 = map(int, sys.stdin.readline().split())
#         if n1 in computer_graph:
#             computer_graph[n1].append(n2)
#         else:
#             computer_graph[n1] = [n2]
    
#     search = BFS(computer_graph, 1)
#     print(len(search) - 1)

# main()