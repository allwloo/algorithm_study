import sys
queue = []
for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    if order[0] == 'pop':
        try:
            print(queue[0])
            del queue[0]
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'back':
        try:
            print(queue[len(queue)-1])
        except:
            print(-1)
    elif order[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        queue.append(order[1])