#백준 11723 집합
import sys

M = int(sys.stdin.readline().rstrip())
check = 0
for _ in range(M):
    command = sys.stdin.readline().split()
    # all <- [0],   add n <- [0] [1]
    if command[0] == 'empty':
        check = 0
    elif command[0] == 'all':
        check = (1 << 21) - 1
    else :
        n = int(command[1])
        if command[0] == 'add':
            check = check | (1 << n)
        elif command[0] == 'toggle':
            check = check ^ (1 << n)
        elif command[0] == 'remove':
            #check = check & (((1 << 21) - 1) ^ (1 << n))
            check = check & (check ^ (1 << n))
        elif command[0] == 'check':
            if check & (1 << n) == 0:
                print(0)
            else:
                print(1)