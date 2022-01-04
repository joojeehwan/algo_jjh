'''

3의 배수 판정 = > 각 자리 숫자의 합이 3의 배수 인것을 찾으면 된다,,!


이진수 n을 십진수로 전개하면서 곱해지는 2의 값을 앞의 계수를 하나씩 더해서 각항을 3의 배수로 만들면서 발생한 항등을 따로 모은다.

(값을 더하고 뺴는 스킬을 사용함)

3의 배수로 묶인 녀석은 이제 더이상 볼필요 없고, 그 앞에  + - 가 번갈아 나오는 녀석의 합이 3의 배수라면

그 값은 3의 배수 인것!

'''







'''
컴비네이션을 아래와 같은 형식으로 구하는 것 중요! 


이걸 어떻게 dfs로 풀 생각을 해? 정말 대단하다,,

재귀가 진짜 중요하구나! 
'''

# 이진수의 3의 배수
Combination = [([-1] * 51) for _ in range(51)]

def calc_combination(nn, kk):
    # nn개 중에서 순서 상관없이 kk개를 고르는 경우의 수
    if nn < kk : return 0 # 자리의 개수보다 넣어야 하는 bit의 개수가 많은 경우는 불가능
    if kk == 0 : return 1
    if kk == nn : return 1
    if kk == 1 : return nn
    if Combination[nn][kk] != -1:
        return Combination[nn][kk]
    now = calc_combination(nn - 1, kk) + calc_combination(nn - 1, kk - 1)
    #공식을 사용해서
    Combination[nn][kk] = now
    return now





t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    neg = n // 2  # 음수 bit 수
    pos = n - neg # 양수 bit 수
    # 음수에 k개의 bit를 전부 할당 -> 양수에 k개의 bit를 전부 할당
    pos_digit_cnt = 0 # 양수 bit에 1을 할당한 개수
    neg_digit_cnt = k # 음수 bit에 1을 할당한 개수

    ans = 0
    for sum in range(-k, k + 1, 2):
        # sum : 각 bit의 값을 더한 값
        if sum % 3 == 0:
            # 양수의 개수와 음수의 개수가 알맞는 조합
            ans += calc_combination(pos, pos_digit_cnt) * calc_combination(neg, neg_digit_cnt)
        pos_digit_cnt += 1
        neg_digit_cnt -= 1

    print(f"#{tc + 1} {ans}")







