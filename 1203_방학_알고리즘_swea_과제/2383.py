'''


와 이건 솔직히 너무 많이 어렵다,,!

풀이가 이해가 안되네?! 답을 봐도?!



시뮬레이션 + dfs 합친,, 어렵다,,

부분집합?!


와 이게 어렵네 참네 참네

이건 내것이 아니다
'''


def on_stair(time_list, stair_num):
    time, wait = 0, 0
    now = []
    #이동중인 사람이나 대기중인 사람, 내려가는 사람이있다면 반복

    while time_list or wait or now:
        #대기 하는 사람이 있다면
        while wait:
            if len(now) >= 3:
                break
            now.append(stair_num[2])
            wait -= 1
        #내려가는 인원이 있을 떄 동작
        for i in range(len(time_list)-1, -1, -1):
            #시간을 감소시키고
            time_list[i] -= 1
            #다 내려갔으면 안녕!
            if time_list[i] <= 0:
                time_list.pop(i)
                wait += 1
        #이동중인 사람이 있다면
        for i in range(len(now) -1, -1, -1):
            #거리를 감소
            now[i] -= 1
            #계단까지 갔다면
            if now[i] <= 0:
                now.pop(i)
        #1초 증가
        time += 1
    return time



def dfs(idx):
    global result
    if idx == M:
        stair_list1, stair_list2 = [], []
        #1번 계단 / 2번 계단 분리하기
        for i in range(M):
            if check[i] == 1:
                stair_list1.append(dist_stair1[i])
            else:
                stair_list2.append(dist_stair2[i])
        result = min(result, max(on_stair(stair_list1, stairs[0]), on_stair(stair_list2, stairs[1])) + 1)
        return
    #부분 집합 로직이 실행되는 곳,,!
    check[idx] = 1
    dfs(idx + 1)
    check[idx] = 2
    dfs(idx + 1)

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    
    #사람위치
    peoples = []
    #계단위치, 계단 값
    stairs = []



    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                peoples.append((i, j))

            elif MAP[i][j] >= 2:
                stairs.append((i, j, MAP[i][j]))
                
                
    #사람의 계단마다 거리계산

    M = len(peoples)

    #사람의 수 만큼 계단까지의 거리를 각각 넣어 둘려고!
    dist_stair1 = [0] * M
    dist_stair2 = [0] * M
    for i in range(M):
        px, py = peoples[i]
        dist_stair1[i] = abs(stairs[0][0] - px) + abs(stairs[0][1] - py)
        dist_stair2[i] = abs(stairs[1][0] - px) + abs(stairs[1][1] - py)

    result = 9876543210
    check = [0] * M
    dfs(0)
    print(f"#{tc} {result}")