''''


최적화문제를 푸는 방법중의 하나로 그리디 알고리즘이 있는 것! => 그리디가 반드시 최적해를 구한다는 보장은 없음.


동전 거스르기는 그리디가 적용이 안되면 DP로 푼다!(혹은 백트래킹)

<>






배낭 짐싸기,, 이거 기억난다 알고리즘 수업때 직접 구현은 안했지만

위의 문제를 그리디 하게 구현 가능?!

내가 선택한 물건의 무게의 합의 배냥의 용량을 초과하지 않으면서 가치가 최대가 되로록!

1) 0-1 물건을 쪼갤 수 없는 경우
=>값이 비싼 물건부터 채운다!

"최적이 아니다"

=> 가벼운 물건부터 채운다!

"최적이 아니다"

=> 무게당 값이 높은 순서로 물건을 채운다.
이것도 그리디가 안됨!


2) Fractional 물건을 쪼갤 수 있음

=> 그리디 적용됨

'''



''''

회의실 배정하기

시작, 종료 시간

겹치는 회의는 동시에x 

가능한 많은 회의가 열리기 위해서는 어떻게 배정?! 


"활동선택문제"

종료 시간이 빠른 순서로 활동들을 정렬
첫번째 활동을 선택
첫번쨰 활동의 종료시간 이후에 가장 빠른 것들을 선택! 
위 과정을 반복 

수도코드 상에서 FOR문에 2 -> N이 아니라 J+1 -> N으로 수정! 


이걸 재귀로도 가능..! 그게 바로 DFS! 


WHIE 문 설명 : 이전의 종료시간 이후에 시작하는 활동중에 ,  가장 빠른,,활동 선택

이 재귀 이해가 안되네,,



탐욕 VS DP




'''


'''

베이비 진 탐욕기법 해결!1

카운트 배열을 만들어서!! 그 숫자가 몇번쓰였느지!! 

1) 모듈려 연산을 활용해서 카운트 배열 만들기!


2) 트리플릿 찾아서 (카운트배열의 값이 3이상) 카운트 배열 -3 하기!, 트리플 개수 값 추가 
컨티뉴 중요!!! => 값이 6이면 트리플릿이 런이 2번 일 수도 있자나!

3) 런 찾기!  여기도 컨티뉴 주어서 같은 자리에서 런 2번찾기! 

4) 런 하고 프리플이 2개가 되면 이제 함수를 종료시켜도 된다


순열 다 찾아서 하는 것보다 효율적 !

아아!! 마지막에서도 런 감사를 할려고 카운트 배열을 12개 만듬!! =>실제로는 마지막에 런이 있을리가 없지만! (따로 무엇이 이루어지는 것은 아닌다!)  그 이전에는 있을 수 있으니깐 \
인덱스를 맞게 할려고 그렇게 하는 것! (관리할려고!!) 인덱스 넘치는거 처리할려고!! 미리 처리하는것!!

'''