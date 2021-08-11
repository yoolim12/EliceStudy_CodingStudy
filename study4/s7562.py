'''
1. 현 위치에서 dir의 값을 더한 좌표값들을 구한다.
2. bfs를 이용하여 모든 경우의 수를 구해본다.(만일 현재까지 나온 최소의 경우의 수와 같아지는 순간 break하고 다음 경우를 계산)
3. 만일 이동 수의 최솟값보다 작은 값이 나오면 그것을 최솟값으로 지정.
'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(first_x, first_y, move_x, move_y):
    dir = [(1,2), (-1,2), (2,1), (-2,1), (1,-2), (-1,-2), (2,-1), (-2,-1)]

    cur_x = first_x
    cur_y = first_y

    for direction in dir:
        pass


def main():
    testnum = int(input())

    for i in range(testnum):
        length = int(input())
        first_x, first_y = map(int, input().split())
        move_x, move_y = map(int, input().split())

main()