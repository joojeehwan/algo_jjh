

#brute force



pattern = "ABC"

text = "ABABCA"



for i in range(len(text) - len(pattern)):
    for j in range(len(pattern)):
        if text[i + j] == pattern[j]:
            j += 1
        else:
            break
    
    
    print("동일함")
    break




'''
    

kmp알고리즘 

=> 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 
불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

패턴을 전처리 하여 배열 next[M]을 구해서 잘못된 시작을 최소화 함!

KMP 알고리즘의 경우에는 접두사와 접미사가 같은 최대길이를 저장하는 배열을 만들어 앞에서부터 검사를 진행하였다면,
       
    
'''





#건너뛰기 배열 만듬 LPS
def computeLPS(pat, lps):
    leng = 0  # length of the previous longest prefix suffix

    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    # Preprocess the pattern
    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif pat[j] != txt[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == M:
            print("Found pattern at index " + str(i-j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lps[j-1]


'''

보이어 무어 알고리즘

=> 문자열은 앞부분 보다는 뒷부분에서 불일치가 일어날 확률이 높다는 성징을 활용!

SO => 오른쪽 끝 부터 비교


KMP 알고리즘과 같이 건너뛰는 경우를 저장하는 배열(skip_table)을 만들어야 합니다. 
이때 배열은 본문 문자열이 비교 문자열에 존재하는지, 존재한다면 불일치 시 얼만큼 건너뛰는지를 판단하는 정보를 가지고 만들게 됩니다.

value의 의미는 '문자열에 불일치가 일어나면 마지막 문자를 기준으로 skip_table의 value만큼 뒤로 이동시키겠다' 입니다.


비교 문자열의 각 문자마다 건너뛰는 value 값을 가지는 skip_table이 만들어져야 합니다. 
value의 의미는 '문자열에 불일치가 일어나면 마지막 문자를 기준으로 skip_table의 value만큼 뒤로 이동시키겠다' 입니다. 
각 문자의 value는 비교문자열 길이(length) - 문자열 index - 1 중 0을 제외한 최솟값으로 계산할 수 있습니다. 
이외 모든 문자는 비교문자열의 길이(length)로 계산합니다.

'''
