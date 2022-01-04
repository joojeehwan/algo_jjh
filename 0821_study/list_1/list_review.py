
#버블소트

'''

인접한 2개의 원소를 비교하면 자리를 교환하는 방식




'''


res = [55, 7, 78, 12, 42]




# len(les) -1을 하는 이유는 인덱스로 하기 때문에 전체 숫자에서 하나를 뺴어 주는것!
# 첫번쨰는 그 숫자까지 포함이 되니깐!
for i in range(len(res) -1, 0, -1):
    # 그 후에 줄어드는 레인지에 맞게 끝까지 변화를 본다
    for j in range(0, i):
        if res[j] > res[j+1]: # 앞에 숫자가 뒤에 숫자보다 크다면
            res[j], res[j+1] = res[j+1], res[j] # 앞과 뒤의 숫자를 바꾼다!


print(res)


# 카운팅 소트
# 카운트를 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다!




DATA = [0,4,1,3,1,2,4,1]


COUNTS = [0] * (4+1)

TEMP = [0] * (8)


for i in range(len(DATA)):

    COUNTS[DATA[i]] += 1 #인덱스를 중심으로 갯수가 얼마나 나왔는지 확인


for j in range(len(COUNTS)-1): #같은 길이의 COUNTS에서 J+1을 검색하니깐!
    # 이렇게 된다!

    COUNTS[j+1] = COUNTS[j] + COUNTS[j+1] #중복합? 을 계속 구함



for i in range(len(TEMP) -1, -1, -1):

    COUNTS[DATA[i]] -= 1 #중복합에서 하나씩 빼면서 그 해당 숫자의 위치를 알아간다,,!
    TEMP[COUNTS[DATA[i]]] = DATA[i]



print(TEMP)







