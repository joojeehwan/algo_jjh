'''



9개의 수 중에서

7개를 뽑아서 합이 100이 되면 된다 .

순열 그런 건가?! 9개 중에서 7개 값 뽑아서! 더한 것들 경우의 수 다 만들어서!

그게 100이 되는 것! 확인하기!


쉽게 생각해서,,, 흠흠,, 2개 뺴서 값이 100이 되는게! 맞다!


7명을 뽑는게 아니라 2개를 뺴서 그게 100인지 확인 해보자!


값을 알아서 remove함수 사용해서 뺴버리는것도 좋네,,!



'''


#
# #기본 입력
# height = []
# for i in range(9):
#     height.append(int(input()))
#
#
# height.sort()
#
# result = sum(height)
#
# for i in range(9):
#     for j in range(i+1, 9):
#         if result-height[i]-height[j] == 100:
#             for k in range(9):
#                 if k == i or k == j: #빼서 값이 100이 되는 인덱스를 찾아서 뺴버린다!
#                     continue
#                 else:
#                     print(height[k])


import sys

height_lst = []

#입력받기
for _ in range(9):
    height = int(sys.stdin.readline().rstrip())
    height_lst.append(height)

# print(height_lst)

#입력받고 오름차순 정리
sorted_height_lst = sorted(height_lst)

#전체합 구하기

total_sum = sum(sorted_height_lst)

for i in range(8):
    for j in range(i+1, 9):
        if total_sum - sorted_height_lst[i] - sorted_height_lst[j] == 100:
            #요기서 continue를 쓰면 그것만 무시가 가능하다는 생각,,!
            for k in range(9):
                if k == i or k == j:
                    continue
                print(sorted_height_lst[k])
                exit()








#으 바보야! 점하나 찍고 플레이를 하면 되거늘!!


'''


9명의 키 값을 입력 받고, 2개를 빼서 그 값이 100이 되는 조합을 찾으면 될거 같다! 


출력시에 일곱 난쟁이의 키를 오름차순으로 출력


리스트로 입력받아서 for / while문 돌면서 합이 100이 될때 멈추고

그 리스트르 하나씩 출력하면 될거 같은데?!


근데 입력 받을 때 리스트를 오름차순 정렬해서 받으면 계산할때 편해질거 같다! 

왜냐면 그래야 for / while문 돌떄 끝에 갔을때 100이 되고 안되고를 명확히 알 수 있을거 같다.

원래는 랜덤하게 2개씩 뺴가는 거 엿을테데
아 그런데 내가 정렬을 했기 떄문에 앞에서부터 2개씩 뺴면서 확인해 가면 
가능하구나! 

점 하나 잡고 검색하는 플레이 잊지 말아라! 버블 소트나,, 카운팅 소트 할떄 쓰던 스킬이자나! 

슬라이딩윈도우로 풀어도 되는 문제 같다,,! 

'''

# import sys
#
# height_lst = []
#
# #입력받기
# for _ in range(9):
#     height = int(sys.stdin.readline().rstrip())
#     height_lst.append(height)
#
# # print(height_lst)
#
# #입력받고 오름차순 정리
# sorted_height_lst = sorted(height_lst)
#
# #전체합 구하기
#
# ans = []
# de = 1
# total_sum = sum(sorted_height_lst)
# for i in range(len(sorted_height_lst)- 2 + 1):
#     temp = 0
#     for j in range(i, i + 2):
#         temp = sorted_height_lst[i] + sorted_height_lst[i+1]
#
#     if total_sum - temp == 100:
#         ans = sorted_height_lst[i+1:]
#         break
#
# print(ans)


s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.remove(two)
s.sort()
for i in s:
    print(i)





























