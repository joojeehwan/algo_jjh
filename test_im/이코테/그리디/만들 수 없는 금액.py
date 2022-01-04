'''

문제 해결 아이디어

1. 화폐 단위를 기준으로 오름차순 정렬

2. 이후에 1부터 차례대로 특정한 금액을 만들 수 있는지 확인한다.

3. 1부터 target - 1까지의 모든 금액을 만들 수 있다고 가정
  우리는 화폐 단위가 작은 순서대로 동전을 확인하며, 현재 확인하는 동전을 이용해 target 금액 또한 만들 수 있는지 확인하면 된다.
  만약 target 금액을 만들 수 있다면, target 값을 업데이트하는 (증가 시키는 ) 방식을 사용.

'''

N = int(input())

lst = list(map(int, input().split()))

lst.sort()

#print(lst)

target = 1

for num in lst:

    if target < num:
        break

    target += num

print(target)