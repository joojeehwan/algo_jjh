'''


무게가 1인 볼링공 : 1개
무게가 2인 볼링공 : 2개
무게가 3인 볼링공 : 2개

이때 A가 특정한 볼링공을 선택했을 때, 이어서 B가 볼링공을 선택하는 경우를 차례때로 계산하여 
문제를 해결할 수 있다. A를 기준으로 무게가 낮은 볼링공부터 무게가 높은 볼링공까지 순서대로 하나씩 확인한다고 했을 떄,,! 

STEP1 A가 무게가 1인 공을 선택할 때의 경우의 수는
1(무게가 1인 공의 개수 ) * 4 (B가 선택하는 경우의 수) = 4가지 경우

STEP2 A가 무게가 2인 공을 선택할 때의 경우의 수는
2(무게가 2인 공의 개수 ) * 2 (B가 선택하는 경우의 수) = 4가지 경우


STEP3 A가 무게가 3인 공을 선택할 때의 경우의 수는
2(무게가 3인 공의 개수 ) * 0 (B가 선택하는 경우의 수) = 0가지 경우


단계가 진행됨에 따라, "B"가 선택하는 경우의 수는 줄어드는데, 이미 계산했던 경우(조합)는 제외하기 때문

'''

n, m = map(int, input().split())
weights = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트 => 0kg은 없으니깐 이런식으로 적는 것!
array = [0] * 11

for weight in weights:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[weight] += 1


result = 0

# 1부터 m까지의 각 무게에 대하여 처리

for i in range(1, m + 1):
    #1부터 m까지의 각 무게에 대하여 처리
    n -= array[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n #B가 선택하는 경우의 수와 곱하기



print(result)