def type1(t):
    if t == n:
        print(*arr)
        return
    for i in range(1, 7):
        arr.append(i)
        type1(t+1)
        arr.pop()
def type2(t, num):
    if t == n:
        print(*arr)
        return
    for i in range(num, 7):
        arr.append(i)
        type2(t+1, i)
        arr.pop()
def type3(t):
    if t == n:
        print(*arr)
        return
    for i in range(1, 7):
        if used[i]:
            continue
        arr.append(i)
        used[i] = 1
        type3(t+1)
        arr.pop()
        used[i] = 0
n, m = map(int, input().split())
arr = []
used = [0] * 7
if m == 1:
    type1(0)
elif m == 2:
    type2(0, 1)
elif m == 3:
    type3(0)



