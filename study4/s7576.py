import sys
from collections import deque

input = sys.stdin.readline

def bfs(tomatoBox):
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    #visited = []
    queue = deque()
    today = deque()
    tomorrow = deque()
    day = 0
    
    if day == 0:
        for r in range(len(tomatoBox)):
            for c in range(len(tomatoBox[0])):
                if tomatoBox[r][c] == 1:
                    #visited.append((r,c))
                    queue.append((r,c))
                    today.append((r,c))

    while queue:
        while today:
            queue.popleft()
            cur_x, cur_y = today.popleft()
            for direction in dir:
                x = cur_x + direction[0]
                y = cur_y + direction[1]
                if (x >= 0 and x < len(tomatoBox)) and (y >= 0 and y < len(tomatoBox[0])):
                    if tomatoBox[x][y] == 0:
                        tomatoBox[x][y] = 1
                        #visited.append((x,y))
                        queue.append((x,y))
                        tomorrow.append((x,y))

        while tomorrow:
            today.append(tomorrow.popleft())
        
        day += 1

    #print(tomatoBox)
    
    # 여기까지 왔으면 방문할 수 있는 노드는 다 방문 했다는 것. 이때 아직도 0이 남아있으면 토마토가 모두 익지 못한 상황
    for tomato_row in tomatoBox:
        if 0 not in tomato_row:
            continue
        print(-1) # continue에 안 걸렸으므로 0이 있다는 뜻이니까
        return
    
    # 여기까지 왔으면 0은 없다는 것. 따라서 day를 출력한다.
    print(day-1)


def main():
    tomatoBox = []
    m, n = map(int, input().split())
    
    for i in range(n):
        _list = list(map(int, input().split()))
        tomatoBox.append(_list)
    '''
    # 예외 상황 1: 안 익은 토마토의 사방이 비어있는 경우
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    for r in range(n):
        for c in range(m):
            if tomatoBox[r][c] == 0:
                for direction in dir:
                    x = r + direction[0]
                    y = c + direction[1]
                    if (x >= 0 and x <= n-1) and (y >= 0 and y <= m-1):
                        if tomatoBox[x][y] != -1:
                            break
                    # 여기까지 break 없이 왔다는 것은 x,y 좌표가 범위를 벗어나지 않으면서 토마토 사방이 -1이라는 것
                    if direction == (0,-1):
                        print(-1)
                        return

    # 예외 상황 2: 토마토 박스 안의 토마토가 전부 안 익은 토마토일 경우(박스 안에 토마토가 적어도 하나 있다는 문제 조건에 의해 상자에 토마토가 없는 경우는 없음)
    for r in range(n):
        for c in range(m):
            if tomatoBox[r][c] == 1:
                break
            # 여기까지 break 없이 왔다는 것은 익은 토마토(=1)이 상자 안에 없다는 것
            if r == n-1 and c == m-1:
                print(-1)
                return'''

    bfs(tomatoBox)

main()