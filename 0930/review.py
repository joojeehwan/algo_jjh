#이진수

# 16진수 -> 10진수 -> 2진수
T = int(input().rstrip())


for tc in range(1, T+1):

    print(f"#{tc} ", end = "")

    n, num_16 = input().split()

    n = int(n)

    # num_16을에 있는 16진수를 한자리의 십진수로 바꾼다.
    for i in range(n):#입력받은 16진수의 개수만큼 반복을 돌려야하니깐

        now = num_16[i]

        now_10 = 0

        if "0" <= now <= "9":
            now_10 = ord(now) - ord("0")

        else:
            now_10 = ord(now) - ord("A") + 10

    #한자리 씩 변환한 10진수 값을 2진수로 바꾼다. 비트 연산으로

        for j in range(3, -1, -1): #4자리 2진수 니깐!
            #j는 2진수의 자리수

            if now_10 & (1 << j) == 0:
                print(0, end="")

            else:
                print(1, end="")

    print("")
    
    
#이진수 표현



T = int(input())


for tc in range(1, T+1):

    N, M = map(int, input().split())
    ans = "ON"

    for i in range(N):
        if M & (1 << i) == 0:
            ans = "OFF"
            break
    print(f"#{tc} {ans}")

