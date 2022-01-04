



def check(s):
    
    #s가 회문이면 True를 리턴, 아니면 False를 리턴

    st = 0
    ed = len(s) - 1
    while st<ed and  s[st] == s[ed]:
        st += 1
        ed -= 1

    if st>=ed:
        return True
    return False


def arrcheck():

    #가로 확인

    for row in range(N):
        for j in range(N - M + 1):
            result = cheek(ARR[ROW])



TC = int(input())


for tc in range(1, TC+1):
    N, M = int(input().split())


    ARR = [input() for _ in range(N)] # 얇은 복사때문에 이렇게 해야 함!

