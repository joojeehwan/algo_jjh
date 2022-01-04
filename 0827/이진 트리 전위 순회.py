#
# import sys
# sys.stdin = open("이진트리전위순회_input.txt")
#
# # index 계산 방식
#
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     V = int(input())
#
#     edge = [[] for _ in range(V + 1)]
#
#     for _ in range(V-1):
#         A, B = map(int, input().split())
#         edge[A].append(B)
#
#

def preorder(now):

    #now -> next
    print(now, end =" ")

    if G[now * 2 ] != 0 : #왼쪽 자식이 있을때만!
        preorder(G[now * 2]) #왼쪽 자식이 누구인가?
    preorder(G[now * 2 + 1])  # 오른쪽 자식이 누구인가?

    #재귀 작성방식
    #현제 : 매개변수
    #재귀부분의 매개변수에 next를 넣어준다.

    #전위순회 : "나 -> 왼쪽  -> 오른쪽

T = int(input())

for tc in range(T):
    N = int(input())

    G = [0] * (1 << N)# 왜 저거 곱해,,? 최악인 편향구조를 생각해서!
    '''
    0000001 
    0000010 *2
    0000100 *2 의 효과라서! 
    
    '''
    #1차원 배열에서 자식의 위치를 계산,,! 부모에서 자식방향으로 누구 인지 기록!
    for i in range(N-1):
        a, b = map(int, input().split())
        # 부모 -> 자식
        # now -> next
        if G[a*2] == 0:
            G[a * 2] = b
        else:
            G[a * 2 + 1] = b

