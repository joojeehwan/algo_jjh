

n = int(input())


MAP = [[0] * n for _ in range(n)]


char = ord("A")

#오른쪽 아래에서 부터 올라오는 거!

for row in range(n-1, -1, -1):
    for col in range(n-1, -1, -1):
        MAP[row][col] = chr(char)
        char += 1

        if char >= ord("Z") + 1:
            char = ord("A")



for row in range(n):
    for col in range(n):
        print(MAP[col][row],  end= " ")
    print()





