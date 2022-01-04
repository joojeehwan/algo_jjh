''''

주어진 문자열에서
연속 3개의 문자가 IOI 이거나
KOI인 문자열이 각각 몇 개 있는지 찾는 프로그램을 작성하라.

문자열은 알파벳의 대문자로만 이루어진다.

예를 들어 "KOIOIOI"라는 문자열은 KOI 1개 , IOI 2개가 포함되어있다.


'''

#그냥 완전 탐색 돌리면 될 듯!

s = input()

KOI = 0
IOI = 0

#3개의 문자니깐 -2로 인덱스 범위가 넘어가지 않도록 조정

for i in range(len(s) - 2):

    #하나씪 뽑아서 문자열 만들고
    part = s[i] + s[i+1] + s[i+2]
    #일치 여부 확인하고 카운팅

    if part == "KOI":
        KOI += 1

    elif part == "IOI":
        IOI += 1

print(KOI)
print(IOI)
