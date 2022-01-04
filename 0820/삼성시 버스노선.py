'''


0번 시작이 아니네?!

1번 부터 인덱스를 시작해야해!! => 한칸 정도 더 크게 만들어서 시작하다!!


#1) 모든 노선체크


#2) 정류장 미리 계산
# 새롭게 출발한느 버스와 이전에 출발하는 버스 더하고, 이전에서 출발해서 도착하는 것 빼기!



#3) 미리 계산 2




조인!! => 안에 값들이 str이어야해! 
'''

def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1

    return cnt





#1. 모든 노선 체크
T = int(input())
for tc in range(1, T+1):

    N = int(input())

    bus_route =[]

    for i in range(N):
        A, B = map(int, input().split())
        bus_route.append((A,B))

    #내가 확인하고 싶은 정류장의 개수
    P = int(input())
    ans = []

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))



    #이거 진짜 꿀팁! 리스트 안에 있는 int형들 str로 바꾸어서 편하게 출력!
    print(f"#{tc} {' '.join(map(str, ans))}")



#2 정류장을 미리 계산해 놓은 경우!

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #버스 노선의 수


    start = [0] * 5001 #출발 정류장 표시
    end = [0] * 5001
    bus_stop = [0] * 5001


    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    
    #버스 계산 끝
    for i in range(len(bus_stop) -1):
        bus_stop[i + 1] = bus_stop[i] -end[i] + start[i + 1]


    P = int(input())
    print("{}".format(tc), end=" ")
    for i in range(P):
        C = int(input()) #우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end = " ")
    print()



#3 정류장 미리 계산



T = int(input())
for tc in range(1, T+1):
    N = int(input()) #버스 노선의 수


    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input())
    print("{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())  # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=" ")
    print()






