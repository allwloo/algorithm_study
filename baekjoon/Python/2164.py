import sys
import time
card_list = list(range(1, int(sys.stdin.readline())+1))
start = time.time()
while len(card_list)>1:
    del card_list[0]
    if len(card_list) == 1:
        break
    card_list.append(card_list[0])
    del card_list[0]
    if len(card_list) == 1:
        break
    print(card_list)
print("time :", time.time() - start)
print(card_list)