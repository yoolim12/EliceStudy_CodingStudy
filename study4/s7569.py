import sys
from collections import deque

input = sys.stdin.readline

def bfs(box_list):
    dir = [(0,1,0), (0,-1,0), (0,0,1), (0,0,-1), (1,0,0), (-1,0,0)]
    #visited = []
    queue = deque()
    today = deque()
    tomorrow = deque()
    day = 0
    
    if day == 0:
        for b in range(len(box_list)):
            for r in range(len(box_list[0])):
                for c in range(len(box_list[0][0])):
                    if box_list[b][r][c] == 1:
                        #visited.append((r,c))
                        queue.append((b,r,c))
                        today.append((b,r,c))

    while queue:
        while today:
            queue.popleft()
            cur_b, cur_x, cur_y = today.popleft()
            for direction in dir:
                b = cur_b + direction[0]
                x = cur_x + direction[1]
                y = cur_y + direction[2]
                if (b >= 0 and b < len(box_list)) and (x >= 0 and x < len(box_list[0])) and (y >= 0 and y < len(box_list[0][0])):
                    if box_list[b][x][y] == 0:
                        box_list[b][x][y] = 1
                        #visited.append((x,y))
                        queue.append((b,x,y))
                        tomorrow.append((b,x,y))

        while tomorrow:
            today.append(tomorrow.popleft())
        
        day += 1

    #print(tomatoBox)
    
    # 여기까지 왔으면 방문할 수 있는 노드는 다 방문 했다는 것. 이때 아직도 0이 남아있으면 토마토가 모두 익지 못한 상황
    for tomato_box in box_list:
        for tomato_row in tomato_box:
            if 0 not in tomato_row:
                continue
            print(-1) # continue에 안 걸렸으므로 0이 있다는 뜻이니까
            return
    
    # 여기까지 왔으면 0은 없다는 것. 따라서 day를 출력한다.
    print(day-2)


def main():
    box_list = []
    tomatoBox = []
    m, n, h = map(int, input().split())
    
    for _ in range(h):
        for i in range(n):
            _list = list(map(int, input().split()))
            tomatoBox.append(_list)
        box_list.append(tomatoBox)

    # for tomato_box in box_list:
    #     for tomato_row in tomato_box:
    #         if 0 not in tomato_row:
    #             continue
    #         print(0) # continue에 안 걸렸으므로 0이 있다는 뜻이니까
    #         return
    for tomato_box in range(len(box_list)):
        for tomato_row in range(n):
            if 0 in box_list[tomato_box][tomato_row]:
                break
            if tomato_row == n-1:
                print(0)
                return

    bfs(box_list)

main()