import sys

def star(x, y, N):
    if y == N:
        return
    if y%3 == 1:
        for i in range(1, N+1):
            if i%3 == 2:
                print(" ", end='')
            else:
                print("*", end='')
        print()
    else:
        for i in range(N):
            print("*", end='')
        print()
    y += 1
    x += 1
    star(x, y, N)

star(0, 0, int(sys.stdin.readline()))

