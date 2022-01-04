
import sys
sys.stdin = open("모음이 보이지 않는 사람_input.txt")


T = int(input())


for tc in range(1, T+1):



    sen = list(input()) # 이렇게 리스트에 넣어버리면! 바꿀수 가 있음!

    vowel = ['a','e','i','o', 'u']

    for v in range(len(vowel)):
        for i in range(len(sen)):
            if vowel[v] == sen[i]:
                sen[i] = " "

    new_sen = " ".join(sen).split() #리스트 안 공백제거!

    #이렇게 하나 알아갑니다,,1
    '''
    sample_list = ['', 'a', '', 'abc', 'qdsf']
    sample_list = [v for v in sample_list if v]
    sample_list # ['a', 'abc', 'qdsf']
    
    '''
    print("#{} {}".format(tc, "".join(new_sen)))





T = int(input())
for tc in range(T):
    str = input()
    ans = ""
    for now in str:
        if now == "a" or now == "e" or now == "i" or now == "o" or now == "u":
            continue #모음이면 무시
        #자음이면
        ans = ans + now
    print("#{} {}".format(tc + 1, ans))