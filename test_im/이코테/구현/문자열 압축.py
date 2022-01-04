'''

2020 카카오 신입공채

프로그래머스 가서 풀어야 함.

이중포문,,! 
'''


def solution(s):
    # 아 이중 포문 싹 돌리면 되는데!!! 하하!!

    # 초기 정답 => 압축을 못하고 그대로의 글자 수
    answer = len(s)
    # 1개 단위(step) 부터 압축 단위를 늘려가며 확인

    for step in range(1, len(s) // 2 + 1):
        #하나의 STEP에 대해서 아래와 같은 것들을 적용
        compressed = ""
        # 앞에서 부터 step만큼의 문자열 추출
        prev = s[0:step]
        count = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        # step이 증가하면 아래에서 step이 변화!
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1

            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우 라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # 다시 상태 초기화
                prev = s[j:j + step]
                count = 1
        # 남아 있는 문자열에 대해서 처리 => 마지막의 끝나는 상태가 이전 상태와 동일하게 끝나는 경우는 else문에 들어가지 못해서 compressed 처리를 못해서 아래에서 한번 더 하는 것!
        compressed += str(count) + prev if count >= 2 else prev

        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer