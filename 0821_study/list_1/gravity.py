
import sys
sys.stdin  = open("gravity_input.txt")


#내 오른쪽 옆에 있는 빈칸의 수를 counting 하는게 관건!

#테스트 케이스의 갯수를 입력받는다.
tc = int(input())



for t in range(1, tc+1):

    # 방의 가로 길이를 입력받는다.
    N = int(input())

    Height = list(map(int, input().split()))

    res = []

    #j값 기준 값이 큰 것들의 개수를 알면,,!
    # 오른쪽으로 가면서 높이가 나보다 작은것들이 빈칸의 갯수! => 그 만큼 이제 낙차가 생기니깐!
    # 결국 1차원 배열에서 고정을 하나씩 시키면서 나보다 작은 것들의 개수를 구하면 된다!
    #i의 값을 고정하고, 나머지 오른쪽 값들과 비교를 하기 위해서, 이중포문을 사용함!
    for i in range(0, len(Height)):
        cnt = 0 #갱신 cnt
        for j in range(i+1, N):
            if Height[i] > Height[j]:
                cnt += 1
        res.append(cnt)


    maxv = res[0]
    for i in res:
        if maxv < i:
            maxv = i
    print(f"#{t} {maxv}")

'''

그래비티는 1차원 배열로 푸는 문제,,! 이차원 배열로 이상하게 생각하면 한도 끝끝



'''