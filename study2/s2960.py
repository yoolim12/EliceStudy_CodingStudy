# import sys

# def main():
#     n, k = map(int, sys.stdin.readline().split())

#     _list = [i for i in range(2, n+1)]
#     _dic = {i: 0 for i in range(2,n+1)}

#     print(_dic)
#     print(_dic[5])
#     print(min(_dic))

# main()

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    _dict = {i:i for i in range(2,n+1)}
    cnt = 0

    while cnt != k:
        global _min
        _min = min(_dict)
        index = []
        for e in _dict:
            if e % _min == 0:
                cnt += 1
                index.append(e)
                if cnt == k:
                    print(e)
                    break
        for i in index:
            del _dict[i]

main()