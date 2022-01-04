



'''

정렬하면 안돼!! 그건 원형을 훼손하는 거자나!

인덱스를 조정하는 변수를 사용해서 잘 풀었구만!

배열을 전부 돌면서 한번은 상승하는거 찾고, 한번은 하강한느거 찾는,,!

'''


N = int(input())

lst = list(map(int, input().split()))

cnt_up = 1
maxup_cnt = 1
#아까 풀어본 문제랑 똑같다!

#점과 그 앞 고정을 푸는,,!

#i번쨰와 i + 1번쨰를 비교하고!
#만약에 차이가 나버린다!  -> else를 사용해서 1로 초기화!
for i in range(len(lst)-1):
    if lst[i] <= lst[i + 1] :
        cnt_up += 1
    else: #여기에 else를 사용해서 cnt_up를 1로 다시 초기화 하는 부분이,,!

        cnt_up = 1
    #길이가 가장 긴 것 구하기! => max
    if maxup_cnt < cnt_up:
        maxup_cnt = cnt_up

cnt_down = 1
maxdown_cnt = 1
for i in range(len(lst)-1):
    if lst[i] >= lst[i + 1] :
        cnt_down += 1
    else:
        cnt_down = 1
    if maxdown_cnt < cnt_down:
        maxdown_cnt = cnt_down

if maxup_cnt > maxdown_cnt:
    print(maxup_cnt)

else:
    print(maxdown_cnt)






