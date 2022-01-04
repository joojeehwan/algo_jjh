





import sys
sys.stdin = open("단조증가_input.txt")

#
# str_1 = "49"
#
# print(str_1[0]) #4
# print(str_1[1]) #9


#
# for i in range(4,5):
#     print(i)



#인덱스 처리가 중요하구만,,!!

def check_danjo(number):

    number_string = str(number) #이것도 좋은 아이디어! 각 자리수를 쉽게 비교하기 위해서 문자열로!
    for k in range(len(number_string) - 1): #밑에서 인덱스로 k , k+1하니깐! 맨 마지막것까지 인덱스가 돌 필요가 없다!
        if number_string[k] > number_string[k+1]:
            return False

    return True

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    maxv = 0

    for i in range(N - 1): #고정!(맨 마지막 인덱스는 그 앞에서 해결하니깐

        for j in range(i + 1, N): # 고정 시킨 그 다음부터 비교
            temp = lst[i] * lst[i + 1] #값을 곱해봄!

            if check_danjo(temp): #바로 그 곱한값을 비교해야 해서 같은 인덴트!
                maxv = max(maxv, temp) # 곱합값이 단조이면! 기존의 maxv값과 비교해서 큰 값을 넣는다!

    if maxv == 0 : #모든 탐색을 다 돌아도! 단조증가하는 것이 없다면! -1로
        maxv = -1

    print("#{} {}".format(tc, maxv))




