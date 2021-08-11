# z z 같은 경우에는 둘다 36진수일 때만 만족을 하는데, 문제에서 a != b 라고 했으므로 결과가 impossible이 되는것

import sys

def main():
    a, b = map(str, sys.stdin.readline().split())

    # if a == b:
    #     print("Impossible")
    #     return
    
    _dict = {}
    letter_a = []
    letter_b = []

    _value = 0
    for num in "0123456789":
        _dict[num] = _value
        _value += 1
    for alphabet in "abcdefghijklmnopqrstuvwxyz":
        _dict[alphabet] = _value
        _value += 1
    
    for letter in a:
        letter_a.append(_dict[letter])
    for letter in b:
        letter_b.append(_dict[letter])

    letter_a.reverse() # 0 인덱스 부터 순서대로 작은 수 부여하기 위함
    letter_b.reverse()

    print(letter_a)
    print(letter_b)
    
    x = 0
    val_a = 0
    val_b = 0
    cnt = 0
    for notation_a in range(2,37):
        for notation_b in range(2,37):
            sum_a = 0
            sum_b = 0
            for index_a in range(len(letter_a)):
                v = (notation_a ** index_a) * letter_a[index_a]
                sum_a += v
            for index_b in range(len(letter_b)):
                v = (notation_b ** index_b) * letter_b[index_b]
                sum_b += v
            if sum_a == sum_b:
                if sum_a < 2**63 and notation_a != notation_b:
                    cnt += 1
                    x = sum_a
                    val_a = notation_a
                    val_b = notation_b
                    print("sum_a: ", sum_a, sum_b)
                    print("notation: ", notation_a, notation_b)
            if cnt == 2:
                print("Multiple")
                return
    if cnt == 1:
        print(x, val_a, val_b)
    else:
        print("Impossible")

main()