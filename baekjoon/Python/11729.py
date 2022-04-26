import sys

def hanoi(n, pre, se, temp):
    if n == 1:
        print(pre, se)
        return
    
    hanoi(n-1, pre, temp, se)
    print(pre, se)
    hanoi(n-1, temp, se, pre)

n = int(sys.stdin.readline())
print(2**n-1)
hanoi((n), 1, 3, 2)