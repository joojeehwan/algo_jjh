'''

isempty <-> !isempty 로 주로 사용! 

peek : 실제로는 꺼내지 않고 확인하는 과정


스택 문제에서는 보통 정할 수 있다.




스택응용!!

( : 넣는다

) : 이거면 빼서 현재 있는 것과 비교!

근데 스택에 괄호가 남아 있다면,,?짝이 안맞는거다!  or 닫히는 괄호가 나왔는데 stack이 비어 있는 경우


연습문제 1 : 스택 구현
연습문제 2 : 괄호 검사


스택응용 2

Function call

프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리!

함수 호출의 단계를 이해해라! 재귀 이해의 초석!

재귀함수는 다른 함수를 출력하는 것! ㄴ


증가하는 재귀호출? => 사진 확인



재귀호출 교재보면 맨위에 1이 추가 도어야 함


피보나치 수열!

리턴이 갈라진다!


함수안과 밖에 생기는 것들이 저장되는 위치는 다르다!

'''


#
# #스택을 구현
#
# #2가지 방식으로 해보길 권장 함수로 하거나,, 그냥,,
#
# top= -1
#
# s = [0] * 10




def f(i, K):
    if i == K:
        return
    else:
        print(A[i])
        f(i+1, K)



N = 3

A = [10, 20, 30]

f(0, N)


def fibo(n):
    if n < 2 :
        return n

    else:
        return fibo(n-1) + fibo(n-2)



#요런 방식도 있음
def fibo2(n):

    if n >=2 and memo2[n] ==0 : #아직 계산되지 않은 값이면

        memo2[n] = fibo(n-1) + fibo(n-2)

    return memo2[n]


#오 이것도 신기하구만,,! 

def fibo1(n):
    if n >=2 and len(memo1) <=n:
        memo1.append(fibo1(n-1) + fibo1(n-2))

    return memo1[n]




n = 50
memo2 = [0] * (n+1)

memo2[0] = 0
memo2[1] = 1
fibo2(n)


memo1 = [0, 1]


'''


문제풀이 tip
eex)
10 tc

3 피보 3을 구해
9
10
5

입력의 최대값만큼 fibo를 돌려놓아서 메모를 만들어 놓고! 다른 것들은 읽어만 오면 된다! 
'''





'''


함수내에서 쓰는 변수는 잠깐 쓰는 것임! 다른 것들이랑 공유되는게 아니라! 



그냥 변수말고 리스트는 global로 선언하지 않아도되는 이유는 무엇인가요?
=>변수말고 리스트는 밖에서 그냥 쓸 수 있구나,,! 

힙영역에는 공통되는 부분이얌! 


'''



'''
DP


수식이 정리가 되어야 한다!! 공식을 찾아내느것이 최우선! 

1) 재귀
2) 메모이제이션?
3) dp?


'''



def fibo_(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]


n = int(input())

table = [0] * (n + 1)
print(fibo_(n))




def fact(n):

    table[0] = 1
    for i in range(1, n+1):
        table[i] = i * table[i-1]

    return table[n]

n = int(input())
table = [0] * (n+1)
print(fact(n))



'''

DFS : 스택 :=> 내가 왔던 곳으로 다시 돌아가기 위해서,,!! 이상한 곳으로 돌아가는게 아니라! 지나온 경로를 저장하기 위한 용도로 스택을 저장! 
재귀를 사용하면 스택을 사용할 필요 X


BFS : 큐


- 되돌아온다? 탐색 X , 다음 탐색을 위한 준비 


'''


'''



'''


str1 = input().rstrip()
str2 = input().rstrip()

stack = []

for now in str1:
    if now == str2[-1]:
        i = -1
        cnt = 0
        while -len(stack) <= i and -len(str2) < i:
            if stack[i] == str2[i - 1]:
                cnt += 1
            i -= 1
        if cnt == len(str2) - 1:
            for j in range(len(str2) - 1):
                stack.pop(-1)
            continue
    stack.append(now)
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))