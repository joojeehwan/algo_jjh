from collections import deque




n, k = map(int, input().split())

graph = []
data = []

#이차원 배열에서 탐색할려면,,! 이중 포문! 당연해!
#연결구조 구성
for i in range(n):

    # 보드 정보를 한줄로 받은 뒤에
    # 그 for문 바로 아래서 해야! 리셋하면서 다시! 알지?!
    # 여기도 이제 for문이 끝나면 이차배열이 되어있네
    # 이런식으로 하는건 data를 특별히 다룰려고 하기 위함
    graph.append(list(map(int, input().split())))

    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            #(바이러스 종류, 시간, row, col) 값 삽입
            data.append((graph[i][j], 0, i, j))


#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()

#큐 생성
q = deque(data) #그냥 큐에 전체 리스트르 넣는 것!

target_s, target_x, target_y = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#큐에 값이 있는 동안
while q:

    #큐에서 맨 앞 점을 꺼냄

    virus, s, x, y = q.popleft()
    
    #정확히 s초가 지나거나, 큐가 빌때까지 반복
    # 이 종료조건! 일단 큐에서 꺼낸 다음에 확인한다!
    if s == target_s:
        break
        
    #현재 노드에서 4방향 다 확인
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        
        #해당 위치로 이동할 수 있는 경우
        if  0 <= nx < n and 0 <= ny < n:
            #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))


#문제에서 0,0을 1,1 로 보고 있다! 그래서 -1 씩 빼는 것!
#우리는 0, 0으로 보고 있으니!
print(graph[target_x -1 ][target_y - 1])






