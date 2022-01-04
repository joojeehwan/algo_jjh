'''

유니온파인드 문제,,!


크루스칼 알고리즘!

'''

def Find(x):

    #자기 자신이 조상인 경우
    if x == parents[x]:
        return x

    px = Find(parents[x])
    parents[x] = px  #최종 조상 노드를 부모ㅁ배열에 넣는다
    return px



def Union(x, y):
    px = Find(x)
    py = Find(y)

    #둘의 조상이 같아? 그럼 종료
    if px == py:
        return

    parents[py] = px
    global group_cnt
    group_cnt -= 1



T = int(input())




for tc in range(1, T+1):

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    #모든 원소가 자기 자신을 부모로 가지도록 설정
    parents = [i for i in range(n + 1)]

    # group = [1] * (n + 1) #여기에 그룹이 있다.

    group_cnt = n # 총 그룹수

    for i in range(0, len(data), 2):
        Union(data[i], data[i + 1])

    print(f"#{tc} {group_cnt}")
