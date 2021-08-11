import sys
from itertools import permutations

n,m = map(int, sys.stdin.readline().split())

n_list = [i for i in range(1, n+1)]
permutations_list = list(permutations(n_list,m))

for e in permutations_list:
    for el in e:
        print(el, end=' ')
    print()