

'''

비트로 풀어야 함!!




'''



T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    bi = bin(M)[2:]

    # print(bi)

    # print(bi[-N:]) # 뒤에서 부터 N만큼 슬라이싱

    #
    falg = 0
    for i in bi[-N:]:
        if i == "0":
            falg = 1

    if falg == 1:
        print(f"#{tc} OFF")

    else:
        print(f"#{tc} ON")



# 이진수 표현
T = int(input())

for tc in range(T):
    n, num = map(int, input().split())
    ans = "ON"
    for i in range(n):
        if num & (1 << i) == 0:
            ans = "OFF"
            break
    print(f"#{tc + 1} {ans}")