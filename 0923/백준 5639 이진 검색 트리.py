''''


입력이 특이함

imort sys

sys.stdin.read()

입력 다 받고 ctrl+Z or ctrl+D로 입력 멈추기


전위순회(루트 왼쪽 오른쪽) 입력 => 후위순회(왼쪽 오른쪽 루트) 출력으로
전위순회의 결과를 보고 원래 있는 그래프를 만들어야대?!


오른쪽에서 한칸씩 왼쪽으로 가면서 루트보다 작은 점이 되는 부분이 바로 그 기준점!
=> 그 기준점이 레프트랑 라이트를 나누는 기준!

포인트는 왼쪽과 오른족의 경계선을 찾는 것!!!


전위순회에 맞게 값을 찾고 후위순회로 출력!


- 전위순회
처리(출력)
왼쪽이동
오른쪽이동


'''



def dfs(now, e):
    if now > e:
        return

    div = e + 1

    for i in range(now + 1, e + 1):
        #루트값 보다 값이 커지는 지점이 오른쪽 서브 트리의 시작

        if tree[now] < tree[e]:
            div = i
            break

    dfs(now+1, div-1)
    dfs(div, e)
    print(tree[now])







import sys
sys.setrecursionlimit(1000000)

tree = []
count = 0
# 이 부분을 read로 대체 할 수 있음!
while count <= 10000:

    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

dfs(0, len(tree) - 1)



#####

import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정
    # for문으로 찾으면 안된다. 아래서 설명
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)


pre_order = []
while 1:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)




#### 겨수님 풀이

import sys

sys.setrecursionlimit(100000)

data = list(map(int, sys.stdin.read().split()))
  # split <- 띄어쓰기, \t, \n 모든 공백 기준

def dfs(s, e):
    if s > e:
        return # 비정상적인 구간이 형성되면 정지

    # s~e의 구간에 해당하는 sub tree를 순회
    now = data[s] # 현재 sub tree의 root 값
    mid = e # 구간이 나뉘는 지점
    while now < data[mid]:
        mid -= 1
        # left구간과 right구간이 나뉘는 지점 찾기
    dfs(s + 1, mid) #left구간
    dfs(mid + 1, e) #right구간

    print(now) # 후위 순회 출력

dfs(0, len(data) - 1)