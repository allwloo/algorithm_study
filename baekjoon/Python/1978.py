N = int(input())
N_list = list(map(int, input().split()))
count = 0
for i in range(N):
    bit = 0
    if N_list[i] == 1:
        bit = 0
    elif N_list[i] == 2:
        count += 1
    else:
        for j in range(2, N_list[i]):
            if N_list[i]%j == 0:
                bit = 1
                break
        if bit == 0:
            count += 1
print(count)

