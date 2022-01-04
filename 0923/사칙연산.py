'''


사칙연산


N : 정점의 총 갯수

정점이 단순한 수? 정점번호 + 해당 양의 정수

정점이 연산자? 정점번호 + 연산자 + 해당 정점의 왼쪽 자식 오른쪽 자식의 **정점번호**

정점번호는 1 부터,,


후위순회.,,!


어차피 시작은 그냥 숫자만 있지는 않아!! 맞네!

'''





def postorder(now):
    if now > N:
        return

    if tree[now][2] != 0:
        postorder(tree[now][2])

    if tree[now][3] != 0:
        postorder(tree[now][3])

    #연산자에 계산 결과 업데이트,,오오,,,그래서 마지막에 포스트 오더1에서 시작하고, [1][1]에 답이 있는 것!
    if tree[now][1] == "+":
        tree[now][1] = tree[tree[now][2]][1] + tree[tree[now][3]][1]
    elif tree[now][1] == '-':
        tree[now][1] = tree[tree[now][2]][1] - tree[tree[now][3]][1]
    elif tree[now][1] == '*':
        tree[now][1] = tree[tree[now][2]][1] * tree[tree[now][3]][1]
    elif tree[now][1] == '/':
        tree[now][1] = tree[tree[now][2]][1] / tree[tree[now][3]][1]


T = 10

for tc in range(1, T+1):


    N = int(input())

    # 일단 입력을 받아햐 하는데,, 4개 칸 만들어서 각각 입력 받는게,,!
    tree = [[0] * 4 for _ in range(N + 1)]

    for _ in range(N):

        lst = list(input().split())
        if lst[1].isdigit():
            tree[int(lst[0])][1] = int(lst[1])

        else:
            tree[int(lst[0])][1] = lst[1]
            tree[int(lst[0])][2] = int(lst[2])
            tree[int(lst[0])][3] = int(lst[3])

    postorder(1)
    print("#{} {}".format(tc, int(tree[1][1])))




# def check(n):
#
#     if n == 2 :
#         return "hello"
#
#
# a = check(3)
#
# print(a)


#######################


