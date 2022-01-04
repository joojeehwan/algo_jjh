
'''

<생각하기>>
종류 1과 같이 배열에 저장을 한 후 m의 값에 따라 출력을 바꾸면 된다.

종류 2의 경우는 배열의 아래쪽부터 출력을 하면 된다.

종류 3의 경우는 각 위치에 출력되는 배열의 번호를 적어놓고 생각해 보자.

'''


n, m = map(int, input().split())

#m = 1일때의 파스칼의 삼각형의 모습을 만드는 것,,!
# i 값을 하나씩 늘려가기 위해서,,! for문을 사용해서!
lst = [[0] * (i + 1) for i in range(n)]


#파스칼 삼각형을 만드는 반복문,,!
#일단 이것이 기본이 되고 아랫것들은 인덱스 값을 조정만 한다!
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            lst[i][j] = 1

        else:
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]


#있는 그대로 출력하면 됨.
if m == 1:

    for i in range(n):
        for j in range(i + 1):
            print(lst[i][j], end = " ")
        print()


if m == 2:

    for i in range(n):
        #공백 찍기
        for k in range(i):
            print(" ", end="")
        #숫자 찍기 아래서부터!
        for j in range(n-i):
            print(lst[n-i-1][j], end=" ")
        print()


if m == 3:

    for i in range(n):
        for j in range(i + 1):
            print(lst[n-j-1][n-i-1], end=" ")
        print()



