import sys
stack = []
for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    if order[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        try:
            print(stack[len(stack)-1])
        except:
            print(-1)
    else:
        stack.append(order[1])
