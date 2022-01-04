'''

곱셈의 과정을 표현하라고,,!? 흠흠,,

'''


n = int(input())
m = int(input())
ans = n * m
lst = []

for i in str(m):
    lst.append(i)

for _ in range(len(lst)):
    print(n * (m % 10)) #일의 자리 숫자 하나 찾고
    m = m // 10 # 다음자리 숫자 찾는다!

print(ans)

'''

number = 123 에 대하여! 

1. 10으로 나누어 자릿수 분리하기(10으로 나누기때문에, 1의 자리부터 분리)

a = []
while(number!=0):
    a.append(number%10)
    x = x//10


2. 문자열로 변환 후, 분리하는 방법

 

변수 number = 123에 대하여, list 변수에 원소를 넣어본 결과

a = []
for i in str(number):
    a.append(i)
['1', '2', '3'] 이라는 결과를 얻을수 있다. 각각의 list 원소는 str의 값을 나타내며 int로 활용할 경우, 형변환 시켜주면 된다. 


3. map 함수를 활용하여 원소값 더하기

sum(map(int, str(number))
python에서 map함수는 다양하게 이용되며, doc에서의 설명은 다음과 같다.

"반복 가능한 모든 항목에 함수를 적용하고 list of results를 반환한다. 만약 추가 반복 가능한 인수가 전달되면 ,
함수는 많은 인수를 취해야하며 모든 반복 가능 항목에 병렬로 적용된다. 
인수가 여러개인 경우 map()은 모든 iterable의 해당 항목을포함하는 튜플로 구성된 list를 반환한다. 
(일종의 transpose 연산) 반복 가능한 인수는 시퀀스 또는 반복 가능한 객체일수 있습니다; 결과는 항상 list입니다."

 

'''