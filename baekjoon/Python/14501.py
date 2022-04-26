import sys
day = [0]*int(sys.stdin.readline())
work, time = [0]*len(day), [0]*len(day)
last_money = []
for i in range(0, len(day)):
    time[i], work[i] = map(int, sys.stdin.readline().split())
for k in range(0, len(day)):
    money = 0
    bit = 0
    day = [0]*len(day)
    for i in range(0, len(day)):
        if i+k >= len(day):
            break
        if day[i+k] != 1:
            if i+k + time[i+k] <= len(day): # i+k부터 시작해서 가능한 수 찾음
                for j in range(time[i+k]):
                    day[i+j+k] = 1
                money += work[i+k]
        if day[i] != 1:
            if i + time[i] <= len(day): # i+k부터 시작해서 가능한 수 찾음
                for j in range(time[i]):
                    if day[i+j] == 1:
                        bit = 1
                        break
                    day[i+j] = 1
                if bit != 1:
                    money += work[i]
            last_money.append(money)
        print(day)
print(last_money)
print(max(last_money))




