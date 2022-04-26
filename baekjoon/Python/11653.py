N = int(input())
number_list = []
for i in range(2, N):
    if N%i == 0:
        number_list.append(i)
        N = N/i
        print(N)
print(number_list)

N = list(int(input()) for _ in range(2))
a = []
for i in range(N[0], N[1]+1):
    bit = 0
    if i == 1:
        bit = 1
    if i == 2:
        a.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                bit = 1
                break
        if bit == 0:
            a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(a[0])
