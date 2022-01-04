n = int(input())

MAP = [[" "] * (2*n - 1) for _ in range(2*n - 1)]


#print(lst)


char = "A"
x = 0
y = n-1
count = n

#왼쪽 아래, 오른쪽 아래, 오른쪽 위, 왼쪽 위
# dir = [1,2,3,4]

while True:

    for i in range(count - 1):
        #일단 처음에 숫자 넣기!
        MAP[x][y] = char
        x += 1
        y -= 1
        #그 다음 알파벳 구하고, 넣기
        #일단 숫자로 바뀌서 +1 해서 다음 구하고! 알파벳으로 구하기
        char = chr(ord(char) + 1)
        #알파벳 숫자 다 돌게 되면 다시 A가 나오도록 해야 한다
        if ord(char) == ord("Z") + 1:
            char = "A"

    for i in range(count - 1):

        MAP[x][y] = char
        x += 1
        y += 1
        char = chr(ord(char) + 1)
        # 알파벳 숫자 다 돌게 되면 다시 A가 나오도록 해야 한다
        if ord(char) == ord("Z") + 1:
            char = "A"

    for i in range(count - 1):

        MAP[x][y] = char
        x -= 1
        y += 1
        char = chr(ord(char) + 1)
        # 알파벳 숫자 다 돌게 되면 다시 A가 나오도록 해야 한다
        if ord(char) == ord("Z") + 1:
            char = "A"

    for i in range(count - 1):

        MAP[x][y] = char
        x -= 1
        y -= 1
        char = chr(ord(char) + 1)
        # 알파벳 숫자 다 돌게 되면 다시 A가 나오도록 해야 한다
        if ord(char) == ord("Z") + 1:
            char = "A"

    #맨 위 갔다가 이제 다음 마름모의 맨위 시작 문자로 가기 위해서!
    x += 1
    #겉의 마름모 부터 안의 마름모까지 n의 숫자만큼 해야하기 떄문에!
    count -= 1
    if count == 0:
        if ord(char) == ord("Z") + 1:
            char = "A"
        # 마지막 안의 마름모!
        MAP[x-1][y] = char
        #이제 그만 반복해라!
        break

for i in range(2*n - 1):
    for j in range(2*n - 1):

        print(MAP[i][j], end = " ")

    print()

