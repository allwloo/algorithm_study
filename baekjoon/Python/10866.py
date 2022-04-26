import sys
deque = []
for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    if order[0] == 'pop_front':
        try:
            print(deque[0])
            del deque[0]
        except:
            print(-1)
    elif order[0] == 'pop_back':
        try:
            print(deque.pop())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        try:
            print(deque[0])
        except:
            print(-1)
    elif order[0] == 'back':
        try:
            print(deque[len(deque)-1])
        except:
            print(-1)
    elif order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'push_front':
        deque.insert(0, order[1])