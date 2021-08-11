_stack = []

def push(x):
    _stack.append(x)

def pop():
    if empty():
        return -1
    else:
        pop_elem = _stack[-1]
        del(_stack[-1])
        return pop_elem

def size():
    return len(_stack)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def top():
    if empty():
        return -1
    else:
        return _stack[-1]

def main():
    n = int(input())
    ans = []

    for num in range(n):
        sentence = input()

        if "push" in sentence:
            l = ""
            for i in range(5, len(sentence)):
                l += sentence[i]
            l = int(l)
            push(l)
        elif sentence == "pop":
            ans.append(pop())
        elif sentence == "size":
            ans.append(size())
        elif sentence == "empty":
            ans.append(empty())
        else:
            ans.append(top())
    
    for e in ans:
        print(e)

main()