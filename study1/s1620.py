num, test = map(int, input().split())
_num_name = {}
_name_num = {}
_test = []

for i in range(1, num+1):
    pokemon = input()
    _num_name[i] = pokemon
    _name_num[pokemon] = i

for i in range(test):
    t = input()
    if t[0] in "123456789":
        t = int(t)
        _test.append(_num_name[t])
    else:
        _test.append(_name_num[t])

for e in _test:
    print(e)

#########시간 초과된 코드##########
# num, test = map(int, input().split())
# _list =[0]
# _test = []

# for i in range(1, num+1):
#     pokemon = input()
#     _list.append(pokemon)

# for i in range(test):
#     t = input()
#     if t[0] in "123456789":
#         t = int(t)
#         _test.append(_list[t])
#     else:
#         _test.append(_list.index(t))

# for e in _test:
#     print(e)