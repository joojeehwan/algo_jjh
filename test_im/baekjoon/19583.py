'''


싸이버 개강 총회

집합을 이용하라는 힌트,, 중복이 없어지겟구먼?!


이게 어떻게 근데 시간 비교를 하나? 그냥 해도 되나?


오 이거 입력어떻게 받지!? 사람 수가 주어진게 아닌디? 그냥 전체 다 받아버려야 하는데??

검색 go


출석확인 ?

1) 개강 총회 시작 전에 채팅 기록이 있는지 
=> set에 담고

2) 개강 총회가 끝난 직후 부터 스트링밍이 끝날때까지 채킹 기록이 있는지를 확인
=> set에 담고

두개 비교해서 같은 것의 갯수 반환하면 될거 같은데?!


'''


# # 와 이렇게 해도 대소비교가 되는구나~
# a = "21:30"
#
# b = "21:35"
#
# if a < b :
#     print("이게 된다고?")
#
# else:
#     print("이거 안되지~")


import sys

input = sys.stdin.readline

start_time, end_time, end_streaming_time = input().split()

#read로 받으니깐 뒤에 /n 이런거 없네?
lst = sys.stdin.read().split()

#['21:30', 'malkoring', '21:33', 'tolelom'] 이런식으로 입력이 들어옴.

chattings_time_id = []

#이차원 배열로 나누고 싶다! 홀짝
for i in range(len(lst) // 2):

    chattings_time_id.append([lst[2*i], lst[2*i + 1]])

# print(chattings_time_id)


metting_before_list = set()
metting_atfer_list = set()

for time, id in chattings_time_id:

    if time <= start_time:
        metting_before_list.add(id)

    if end_time <= time <= end_streaming_time:
        metting_atfer_list.add(id)


print(len(metting_before_list & metting_atfer_list))


