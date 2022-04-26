import sys
sum2 = []
for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    if k == 0:
        sum2.pop()
    else:
        sum2.append(k)
print(sum(sum2))
