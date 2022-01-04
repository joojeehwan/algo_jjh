'''
첫째 줄에 점수 N이 정수로 주어진다.
(10 ≤ N ≤ 99,999,999)
단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.
'''


N = list(input())

center = len(N)//2

left_sum = sum(map(int, N[0:center]))
right_sum = sum(map(int, N[center:]))

if left_sum == right_sum:
    print("LUCKY")

else:
    print("READY")

