

'''

col이 홀짝일떄를 구분 해야 할거 같다!


'''


n = int(input())

MAP = [[0] * n for _ in range(n)]

char = ord("A")


# 아니 이걸 i 기준으로 한다구?! 아아 이걸 col에 넣으면 그게 바로,, col 기준이지!

'''

나는 바보 같이 for for if 를 할려고 했다
for if for을 했어야 했는데!
'''

for i in range(n):

    if i % 2 == 0:

        for j in range(n):

            MAP[j][i] = chr(char)
            char += 1

            if char >= ord("Z") + 1:
                char = ord("A")
    else:

        for j in range(n-1, -1, -1):

            MAP[j][i] = chr(char)
            char += 1


            if char >= ord("Z") + 1:
                char = ord("A")


for row in range(n):
    for col in range(n):
        print(MAP[row][col], end = " ")
    print()