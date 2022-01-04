'''


슬라이딩 윈도우 기법 적용

https://kimmeh1.tistory.com/407

인덱스 처리에 주의 => 모듈러 연산 "%"을 사용해야 함.

회전초밥

1. 회전 초밥에서 연속적으로 k개의 초밥을 선택

2. 각 초밥 번호를 집합에 넣는다 -> 집합의 특성상 중복되는 번호가 없기 떄문에 

3. 쿠폰 번호가 집합에 속하지 않았다면, 집합 크기 + 1 종류의 초밥을 먹은 것

초밥을 처음 선택할 시작점을 바꿔가며 연속적으로 k개의 초밥을 선택


아,, 모듈러 연산을 하기 싫어서 거꾸로 한번 이어 붙엿구나,, 오오,, 대단하네,,,




'''

#단순 반복 완전 검색





def max_sub_array(arr, k):

    max_sum = 0
    arr_size = len(arr)


    for i in range(arr_size - k + 1):
        temp_sum = 0

        for j in range(i , i + k):
            temp_sum += arr[j]

        max_sum = max(max_sum, temp_sum)

    return max_sum




def sliding_window(arr, k):

    window_sum = 0
    max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end] # 슬라이딩 인덱스 범위 요소 합산
        #슬라이딩 윈도우

        if window_end >= (k - 1) :
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # 슬라이드 윈도우 범위를 벗어난 요소를 합계에서 제거
            window_start += 1 #슬라이드 윈도우 시작 인덱스 증가


    return max_sum



from collections import deque

# #슬라이딩 윈도우 기법을 사용
N, d, k, c = map(int, input().split())


lst = []

for i in range(N):

    lst.append(int(input()))


#회전하기 때문에 추가되는 범위 만큼 더 이어 붙인다.
lst += lst[:k-1]

ate = [0 for _ in range(d+1)]

window = deque()

cnt = 0

ans = 0

for idx, val in enumerate(lst):

    window.append(val) #윈도우에 값을 넣는다
    ate[val] += 1 #넣은 값을 기록!

    if ate[val] == 1: #처음 들어온 초밥이므로 먹은 초밥의 종류인 cnt를 증가 시킨다. 
        cnt += 1

    if idx < k - 1: #주어진 가짓수 만큼 윈도우에 넣어야 하기 때문에!
        continue

    if ate[c] == 0: #쿠폰 초밥을 먹은적이 없다!
        ans = max(ans, cnt+1) #계속 최대값을 비교하면서,,! 쿠폰 종류를 넣은 것을 최대값으로

    else: #이저엔 쿠폰 초밥이 있는 것을 먹었다
        ans = max(ans, cnt)

    #윈도우에서 가장 첫 번째에 있는 초밥을 제거 했을때 ate의 값이 0이 된다면 cnt 감소
    first_susi = window.popleft()
    ate[first_susi] -= 1

    if ate[first_susi] == 0:
        cnt -= 1

print(ans)



