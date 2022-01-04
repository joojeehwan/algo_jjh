



str1 = "ABCA"

str2 = "ABABCA"


'''

딕셔너리 사용하면 좋을꺼 같다! => 이거 방법 알아내! 

문자별로 몇개가 나오는지 확인하는 것! 

문자별로 

'''
T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    counts = [0] * 256
    # 문자 <- Ascii, 0~127
    # 문자 1개 : 1byte, 8bit, 2진수 8자리 <- 0~255
    # counts[index] = value
    # index : Ascii코드값(0~127), value : 해당 Ascii코드 값의 개수
    # A <- 65, counts[65] 1개 추가
    # 단, 2byte이상의 문자는 저장 X <- 한글, 한자
    for ch in str2:
        counts[ord(ch)] += 1

    max_count = -1
    for ch in str1:
        if max_count < counts[ord(ch)]:
            max_count = counts[ord(ch)]

    print("#{} {}".format(tc + 1, max_count))





#######



test_case = int(input())

for t in range(test_case):
    str1 = input()
    str2 = input()
    s = set([ch for ch in str1])
    dictionary = {ch : str2.count(ch) for ch in s}
    print(f"#{t + 1} {max(dictionary.values())}")

