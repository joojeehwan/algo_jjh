

N = int(input())

lst = list(map(int, input().split()))

def gcd_get_recurion(x, y):

    if y == 0 :
        return x

    return gcd_get_recurion(y, x % y)

gcd = lcm = lst[0]

for i in range(1, N):

    gcd = gcd_get_recurion(gcd, lst[i])
    lcm = lcm / gcd_get_recurion(lcm, lst[i]) * lst[i]

print(int(gcd), int(lcm))
