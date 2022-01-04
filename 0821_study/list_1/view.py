import sys

sys.stdin = open("view_input.txt")


'''

논리의 발전,,!

나를 기준으로 좌우 2칸이 나보다 작으면 되네? 

예외 조건 생각하면서,,ex) 처음 2개랑 마지막 2개는 빌딩이 없고,,! 




'''

for tc in range(1, 11):

    N = int(input())

    building = list(map(int, input().split()))


    print(building)


    sum = 0

    for i in range(2, N-2): #빋딩 하나씩 고정
        #i -< 2 ~ n-3 why? 처음 2개랑 마지막 2개는 안보니깐!
        max_value = 0 # 고정 후 탐색할때, 탐색의 결과를 저장하고 그 다음의 고정지역으로 넘어가야하기 때문에!

        for j in range(-2, 3):
            if j != 0 and max_value < building[i + j]: #0을 제외해서 4가지의 경우의 수를 확인한다!
                #여기서 가장 큰수를 찾고, 가장 큰 값에서 나머지 값들을 뺴가면서 확인하면 된다.
                #빌딩 i+j가 신의 한수!
                max_value = building[i+j]
        '''
        고정 now를 제외하고 그 중에서 가장 큰것을 찾아서! now와 뺀다!
        '''

        ret =  building[i] - max_value #나를 제외하고 그중에서 제일 큰거에서 뺸것!
        if ret < 0: #조망권이 없게 되는 경우들은 0으로 만들어 최종결과에 영향을 미치지 못하게 함
            ret = 0

        sum += ret

        print("#{} {}".format(tc, sum))