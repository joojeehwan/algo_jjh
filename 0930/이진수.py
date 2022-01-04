



# T = int(input())
# #
#
#
# for tc in range(1, T+1):
#
#     N, Hexa = input().split()
#
#     ans = int(Hexa, 16)
#     ans = bin(ans)[2:]
#
#     #함수 사용 방법 이거 사용 안하고 어떻게 하면 되지?!
#
#     print(ans)




# print(ord("A")) # 아스키 코드를 이용하여 문자"9" 를 숫자 9로 바꿀 수가 있구나






#이진수
t = int(input().rstrip())

for tc in range(t):
    print(f"#{tc + 1} ", end = "")
    n, num_16 = input().split()
    n = int(n)
    for i in range(n):
        now = num_16[i]
        # 10진수로 한자리 변환
        now_10 = 0
        if "0" <= num_16[i] <= "9":
            now_10 = ord(num_16[i]) - ord("0")
        else : # "A" ~ "F" = 10 ~ 15
            now_10 = ord(num_16[i]) - ord("A") + 10 #A자체가 10이상의 수니깐
            #'A' ~ 'F' = 65 ~ 81 => 0 ~ 5 => 10 ~ 15
        #print(f"{num_16[i]} : ", now_10)

        #한자리씩 변환한 것을 이제 2진수로 체인지
        for j in range(3, -1, -1):
            # j는 2진수의 자릿수
            if now_10 & (1 << j) == 0: #앤드 연산 : 둘다 일인곳만,,!
                print(0, end = "")
            else:
                print(1, end = "")
    print("")



