import sys
from collections import deque

input = sys.stdin.readline

def bfs(house_map, start_node):
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = [start_node]
    q = deque([start_node])

    while q:
        cur_x, cur_y = q.popleft()
        for direction in dir:
            nx = cur_x + direction[0]
            ny = cur_y + direction[1]
            if (nx >= 0 and nx < len(house_map[0])) and (ny >= 0):
                pass

def main():
    n = int(input())
    house_map = []
    house_count = 0

    for _ in range(n):
        r = input()
        house_map.append(r)
    
    for r in range(n):
        for c in range(n):
            if house_map[r][c] == 1:
                bfs(house_map, (r,c))
                house_count += 1

main()