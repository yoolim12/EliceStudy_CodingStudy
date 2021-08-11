'''
1. 처음으로 1이 나온 지점을 start point로 지정
2. start point에서 dfs 실행
3. dfs 한번 실행할 때마다 count + 1
4. dfs를 통해 visited된 노드들은 모두 0으로 다시 바꿔준다.
'''
import sys

input = sys.stdin.readline
ans = []

def DFS(island_map, start_x, start_y):
    '''
    stack = [(start_x, start_y)]
    cur = (start_x, start_y)

    while stack:
        for direction in dir:
            node_x = cur[0] + direction[0](dir 중에 하나)
            node_y = cur[1] + direction[1]

            if node_x >= 0 and node_y >= 0:
                if island_map[node_x][node_y] == 1 and (node_x, node_y) not in visited:
                    visited.append((node_x, node_y))
                    stack.append((node_x, node_y))
                    cur = (node_x, node_y)
                    break

            if direction == (-1,1): ----> (-1,1)이 될 때까지 break를 하지 않았으므로 위의 조건을 만족 못함
                stack.pop()
                if stack: cur = stack[-1]
    '''
    rownum = len(island_map)
    colnum = len(island_map[0])

    dir = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    visited = [(start_x, start_y)]
    stack = [(start_x, start_y)]
    cur = (start_x, start_y)

    while stack:
        for direction in dir:
            node_x = cur[0] + direction[0]
            node_y = cur[1] + direction[1]

            if (node_x >= 0 and node_x <= rownum - 1) and (node_y >= 0 and node_y <= colnum - 1):
                #print(node_x, node_y)
                if island_map[node_x][node_y] == 1 and (node_x, node_y) not in visited:
                    visited.append((node_x, node_y))
                    stack.append((node_x, node_y))
                    cur = (node_x, node_y)
                    break

            if direction == (-1,1):
                stack.pop()
                if stack: cur = stack[-1]

    return visited

def island_count(island_map, row, col):
    island_num = 0

    for i in range(row):
        for j in range(col):
            #print(i,j)
            if island_map[i][j] == 1:
                visited = DFS(island_map, i, j)
                for elem in visited:
                    x,y = elem
                    island_map[x][y] = 0
                island_num += 1
    
    ans.append(island_num)

def main():
    while True:
        island_map = []
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        for row in range(h):
            _list = list(map(int, input().split()))

            island_map.append(_list)
        
        island_count(island_map, h, w)
    
    for e in ans:
        print(e)

main()