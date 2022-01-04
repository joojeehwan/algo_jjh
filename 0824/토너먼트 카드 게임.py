




'''





'''

#반복되는 작업을 함수와 재귀를 사용해서 해결


import sys
sys.stdin = open("토너먼트 카드게임_input.txt")


#이것도 dfs문제임,,!

def play_game(i, j): #분활정복,,!


#이거의 구조가 퀵소트랑 비슷하네!!

    #기저 조건..! 두개가
    if i == j :

        return i

    #범위를 둘로 나눔

    left = play_game(i, (i+j)//2)
    right = play_game((i+j)//2+1, j)

    if lst[left] == 1: #가위
        if lst[right] == 2:
            return right
        elif lst[right] == 3 :
            return left
        elif lst[right] == 1:
            return left
    if lst[left] == 2: #바위
        if lst[right] == 1:
            return left
        elif lst[right] == 3 :
            return right
        elif lst[right] == 2:
            return left
    if lst[left] == 3: #보
        if lst[right] == 1:
            return right
        elif lst[right] == 2 :
            return left
        elif lst[right] == 3:
            return left



T = int(input())

for tc in range(1, T+1):

    N = int(input())
    lst = [0] + list(map(int, input().split()))

    print("#{} ".format(tc), end="")
    print(play_game(1, N))
    
    
#교수님 풀이

'''

start , end는 다 인덱스다! 

만약에 둘다 배열이 값이 하나 있으면 start, end가 둘다 0이라서
계속 돈다! 

=> 그래서 기저 조건이 필요해! 



가위바위보 하는 부분이 좀 신기,,! 




'''



# 그래서 누가 이겼냐!
def dfs(start, end):
    # start ~ end범위
    if start == end:
        return start
        # 기저 조건(최대한 쪼개서 1개만 남았는가?)

    mid = (start + end) // 2
    left = dfs(start, mid) # 왼쪽 구간
    right = dfs(mid + 1, end) # 오른쪽 구간

    if data[left] < data[right]:
        if data[left] == 1 and data[right] == 3:
            return left
        else :
            return right
    elif data[left] > data[right]:
        if data[left] == 3 and data[right] == 1:
            return right
        else :
            return left
    else :
        return left

    # 퀵정렬, 병합정렬

T = int(input())
for tc in range(T):
    size = int(input())
    data = list(map(int, input().split()))
    winner = dfs(0, size - 1) #나랑 풀이 다른것은 나같은 경우는 이제 인덱스를 맞춰주기 위해서 [0]을 추가 했기에!
    print("#{} {}".format(tc + 1, winner + 1))



