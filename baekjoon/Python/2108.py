import sys
import math
import time
num = []
cnt = 0
for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
print(round(sum(num)/len(num)))
num2 = sorted(num)
if len(num2)%2==0:
    print(int(num2[int(len(num2)/2)]+num2[(int(len(num2)/2)+1)]/2))
else:
    print(num2[math.floor((len(num2)/2))])

"""

for i in range(0, len(num2)):
    if cnt < num2.count(num2[i]):
        choibin = {}
        choibin[i] = num2[i]
        cnt = num2.count(num2[i])
    elif cnt == num2.count(num2[i]):
        choibin[i] = num2[i]
final = list(choibin.values())
for i in range(len(final)):
    try:
        if final[i] != final[i+1]:
            print(final[i+1])
            break
    except:
        print(final[i])
        break
"""
print(max(num)-min(num))
