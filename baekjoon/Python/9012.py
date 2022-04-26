import sys
for i in range(int(sys.stdin.readline())):
    PS = list(sys.stdin.readline().strip())
    PS.append(0)
    if PS.count('(') != PS.count(')'):
        print('NO')
    else:
        i = 0
        while PS[0] != 0:
            if len(PS) <= i:
                print('NO')
                break
            if PS[0] == ')':
                print('NO')
                break
            if len(PS) == 3:
                i = 0
            if PS[i] == '(':
                if PS[i+1] == ')':
                    del PS[i:i+2]
                    i = 0
            i += 1
        if PS[0] == 0:
            print('YES')