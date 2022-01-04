''''

순열과 가장 크게 다른 점!

중복 여부를 따진다! 순서가 없기 때문에 {1,2,3} 하고 {1,3,2}는 같은 것으로 본다!

'''


#반복문을 통한 조합


# c = 0 #갯수
#
# #지금 이건 10 C 3 을 구현한것! 10개의 숫자 중에서 3개를 뽑는 경우의 가짓수
#
# for i in range(8):
#     for j in range(i + 1, 9):
#         for k in range(j+1, 10):
#             c += 1
#
#             print(c, i, j, k)
#
            
'''

n개에서 r개를 고르는 조합

s : 선택 구간의 시작

k : 고른 개수

'''
def comb(n, r):


    if r == 0:
        print(temp)

    elif n < r:
        return

    else:
        temp[r-1] = comb_lst[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


R = 3
temp = [0] * R
comb_lst = [0,1,2,3,4]
N = len(comb_lst)

comb(N,R)


print("구분")

def nCr(n, r, s = 0, k = 0):


    if k == r:

        print(*comb)

    else:

        for i in range(s, n-r+k+1): #s ~ n-r+k 선택할 수 있는 구간의 끝
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 5
R = 3
comb = [0] * R

nCr(N,R)