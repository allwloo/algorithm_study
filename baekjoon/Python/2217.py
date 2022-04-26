import sys
lope = []
for i in range(int(sys.stdin.readline())):
    lope.append(int(sys.stdin.readline()))
lope.sort()
k = len(lope)
max_kg = lope[0]*len(lope)
for i in range(len(lope)):
    if max_kg < lope[i]*k:
        max_kg = lope[i]*k
    k = k-1
print(max_kg)
    

