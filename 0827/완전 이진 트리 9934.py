


'''

순회의 결과를 보고 그래프를 예상하는..! 반대의 생각 문제 !


깊이가 k이면 노드개수는? 2 ** k - 1 인데 여기서는 2 ** k 이네!



어떤 애들이 어디 있는지 다 파악함,,! 인오더함수!


깊이가 깊어질 수록 자식의 개수가 두배씩 증가함을 알고 출력때 이용 !
=> 한레벨을 출력할 수 있음!

1개,, 2개,,, 4개 출력,,, 이런식임!

'''

def inorder(now, depth):
    global cnt
    global K
    if depth > K:
        return
    inorder(now * 2, depth + 1)
    G[now] = result[cnt] # 이번에 출력된 얘는 cnt번째 얘
    cnt += 1 # 다음은 지금 cnt바로 다음 번호
    inorder(now * 2 + 1, depth + 1)

K = int(input())
G = [0] * (1 << K)
result = list(map(int, input().split()))
# result : inorder의 결과
cnt = 0
inorder(1,1)
cnt = 1
for i in range(K):
    # i : 깊이
    for j in range(1 << i):
        print(G[cnt], end = " ")
        cnt += 1
    print("")