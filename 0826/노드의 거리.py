#추천,, deque사용하는 방법

'''



deque 의 popleft()은 1번,,! 보통의 pop(0)은 앞에 있는 배열의 크기 만큼 시간이,,!


이코테 확인!



'''




'''

그래프를 표시하는 방법,,!  이코테 확인! 


1) 인접행렬 1. 

입력이

4 5
6 7
8 8
.
.
.
.
이런식으로 주어졌을 때! 

G[ROW][COL]을 만들고! N * N 행렬,,!을 만듬! 

단방향 : G[4][6] = 1 OR G[6]][4] =1 

양방향 : G[4][6] = 1 AND G[6]][4] =1 

노드가 많을때 너무 비효율적,,,!! 


2) 인접리스트 방식! 

연결이 된것만 필요! = 연결이 안된것은 필요 X



어느 점에서 갈 수 있는 것은 이미 정보가 있어,,! => 이거 저번에 이해한 그거다,,! 문제풀이 보면서 다시 리뷰!


갈수 없는 점을 확인할 필요가 있나? NO 왜냐면 어차피 간 곳만 저장해 놓았으니깐! 





인접리스트가 안좋을떄는,,! 어디에서 어디로 가는 간선이 존재하는가?를 확인할때

간선에 연결된것이 많을 떄 그러면 간선의 개수만큼 반복을 해야하니간,,!(심지어 랜덤하게 값이 들어간다! 어디에서 어디 갈 수 있는 것이!) 
인행 같은 경우는 어디에서  어디로 연결된것은 배열에서 값하나만 확인하면 되긴해서 앞의 경우는 인행이 더 나음! 




2차원 맵으로 문제에서 주어진다면!애초에 그냥 좌표계산이 목적이니 인접행렬을 쓰는게 낫다! 델타배열도 쓰고 그래야 하니깐!


'''

# BFS

T = int(input())

for tc in range(T):

    V, E = map(int, input().split())

    #1.이차원 리스트 방식
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        FROM, TO = map(int, input().split())
        graph[FROM].append(TO)
    print(graph)

    '''
    2. QUEUE생성
    1) POP, APPEND
    2) 디큐
    3) 프론트 리어 방식,,
    
    '''

    # 2. queue 생성(append, pop활용 version)
    # q = []
    #
    # # 3. 시작점 세팅(시작점을 queue에 추가)
    # q.append(시작점
    # 번호)
    #
    # while len(q) != 0:
    #     # 4. queue에서 맨 앞 점를 꺼냄(now)
    #     # ---- 추가적인 계산이 필요한 경우 여기서
    #     now = q.pop(0)
    #
    #     # 5. now에서 갈 수 있는 모든 점을 찾기(next)
    #     for next in G[now]:
    #         # 6. next를 queue에 추가
    #         q.append(next)

    """
1. 연결 구조를 구성
2. queue 생성
3. 시작점 세팅
----준비---
4. queue에서 맨 앞 점를 꺼냄(now)
5. now에서 갈 수 있는 모든 점을 찾기(next) => 인접행렬 VS 인접리스트 ,, 방법이 달라져! 
6. next를 queue에 넣기
7. 4~6번 단계를 queue가 비워질 때까지

--- 기본 구성 완료 ----
옵션 : 
1. 맵을 벗어나는가? : 2차원맵 한정
2. 갈 수 없는 점 확인
3. 갔던 점을 다시 돌아갈 수 있는가? <- visited배열 활용
   visited : 내가 찾은 점인가?

---- 살짝 응용 ----
1. 몇 번 만에 갈 수 있는가?
   visited : 내가 몇 번만에 찾은 점인가?   visterd[next] = visted[now] + 1 
   내가 나우보다 1번더 가서 찾은 것이다.

실제 BFS가 어디서 활용되느냐!!!!!!!!
1. 제일 적게 다른 점을 들려서 가는 방법
    -BFS에서 어떤 점을 발견하면 그 점이 가장 빠른 타이밍에 발견 된 것이다.

    """


    #와치스에 내가 보고 싶은 변수들을 ㄱ냥 적으면 되는구나!! 와치스 잘 사용해보자,,


# 값 출력할때 비지티드 -1 하는 것,,,!
#시작점 세팅 할때,, 0으로 쓰는 것은 위험,,!  그냥 출력시에 -1 하는게 맞지!
# 간선을 지나 간것을 하나 counnt 해야대는데! 스타트는 지나지 않고도 하자나!



######## 교수님 풀이


from collections import deque

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    """ # 인접 행렬
    G = [ [0] * (V+1) for _ in range(V + 1) ] 
    for _ in range(E):
        FROM, TO = map(int, input().split())
        G[FROM][TO] = 1
        G[TO][FROM] = 1
    """

    """
    # 인접 리스트
    G = [ [] for _ in range(V + 1) ]

    for _ in range(E):
        FROM, TO = map(int, input().split())
        G[FROM].append(TO)
        G[TO].append(FROM)
    """

    G1 = [[0] * (V + 1) for _ in range(V + 1)]
    G2 = [[] for _ in range(V + 1)]
    for _ in range(E):
        FROM, TO = map(int, input().split())
        G1[FROM][TO] = 1
        G1[TO][FROM] = 1
        G2[FROM].append(TO)
        G2[TO].append(FROM)
    # 1. 연결 구조를 구성

    # 2. queue 생성
    q = []  # pop, append
    q = deque()  # deque방식
    q = [0] * (V + 1)  # front, rear
    visited = [0] * (V + 1)

    front = 0
    rear = 0

    # 3. 시작점 세팅
    s, g = map(int, input().split())
    visited[s] = 1  # <- 조심 0의 의미가 이미 있어요(내가 아직 찾지 못한 점이다.)

    q[rear] = s
    rear = (rear + 1) % len(q)

    # 7. 4~6단계를 반복
    while front != rear:
        # 4.queue에서 맨 앞 점를 꺼냄(now)
        now = q[front]
        front = (front + 1) % len(q)
        # 5. now에서 갈 수 있는 모든 점을 찾기(next)
        for next in G2[now]:
            if visited[next] != 0:
                continue
            # 6. next를 queue에 넣기
            visited[next] = visited[now] + 1
            q[rear] = next
            rear = (rear + 1) % len(q)

        """
        # 5. now에서 갈 수 있는 모든 점을 찾기(next)
        for next in range(1, V+1):
            if G1[now][next] == 1:
                # now -> next로 가는 선이 있다!

                #6. next를 queue에 넣기
                q[rear] = next
                rear = (rear + 1) % len(q)
        """
    if visited[g] == 0:
        print("#{} {}".format(tc + 1, 0))
    else:
        print("#{} {}".format(tc + 1, visited[g] - 1))
"""
옵션 : 
1. 맵을 벗어나는가? : 2차원맵 한정
2. 갈 수 없는 점 확인
3. 갔던 점을 다시 돌아갈 수 있는가? <- visited배열 활용
   visited : 내가 찾은 점인가?
   ---- 살짝 응용 ----
1. 몇 번 만에 갈 수 있는가?
   visited : 내가 몇 번만에 찾은 점인가?
"""