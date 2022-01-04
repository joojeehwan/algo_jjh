T = int(input())

for tc in range(1, 1 + T):
    word = str(input())

    res = ''

    for q in word:

        if q != 'a' and q != 'e' and q != 'i' and q != 'o' and q != 'u':
            res += q

    print('#{} {}'.format(tc, res))



'''

T = int(input())
for tc in range(T):
    str = input()
    ans = ""
    for now in str:
        if now == "a" or now == "e" or now == "i" or now == "o" or now == "u":
            continue #모음이면 무시
        #자음이면
        ans = ans + now
    print("#{} {}".format(tc + 1, ans))



'''