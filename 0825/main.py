'''



큐,, 삽입과 삭제의 의취가 제한적인 자료구조


앤큐, 디큐라고 쓰자! 푸쉬 팝 쓰지말고! 큐를 쓸떄는! 가독성,,!! 





- 이스앰티 에다가 낫을 붙쳐서 이스낫앰티처럼 쓴다


p.6

1)
프로트 = 리어 = -1 => 아직까지 저장이 이 안됨! 초기화의 의미!

q[] * 100

front = -1
rear = -1

2) 원소삽입

rear += 1
q[rear] = "a" #enque

3) 원소삽입

rear += 1
q[rear] = "b" #enque


4) 우ㅝㄴ소 반환 삭제

front += 1
data =  q[front]# (값을 리턴하는,,! ) return data


프론트랑 리어나 만나? 큐가 비어있따!





'''


Q = [0] * 10 #10칸 짜리 큐
front = - 1

rear  = -1

rear += 1           #enQueue
Q[rear] = 1

rear += 1         #enQueue
Q[rear] = 2

rear += 1        #enQueue
Q[rear] = 3



while front != rear:
    front += 1
    print(Q[front], end =" ")      #print(deQueue())



listQ = []

listQ.append(1)
listQ.append(2)
listQ.append(3)

while listQ:
    print(listQ.pop(0), end = " ") #팝 제로,,! 라서 가능함!
print

#2개가 같아 보이지만, append가 시간이 많이 걸린다.. 시간이 오래 걸려!

from collections import deque


#enqueue => append
q = deque()
q.append(1)
q.append(2)
q.append(3)

#dequeue => popleft
while q:
    print(q.popleft())

'''


선형 큐 단점 극복,,! 공간이 있어도 풀이라고 인식하는,,!

1) 매 연산이 이루어질때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴(비효율)

2)논리젹으로 원형,,! => 원형큐

모듈러 연산을 사용해서! 




현실세계에서 큐에 삽입하다가 풀? 그냥 덮어쓰이게 만든다! 

버퍼?!



ISFULL?
리어 다음칸이 프론트면!!









--------------------------------------
연결큐,, 개요! 

연속으로 저장할 수 없게 큰 덩어리 이거나 계속 크기가 변해?
잘라서 메모리에 적당한 공간에 찔러 넣는다! 근데 그렇게 멀리 떨어져있어더 서로의 위치를 알아야하니,,!
그래도 저장된 위치를 알아야 하니깐
주소 값을 이어준다! 




<목표>
1. 크기가 정해진 리스트를 활용한 선형큐의 구현
2. 원형큐.. 이런게 있다?,, 우선순위 큐도.. 약간 이런게 있다? 정도! 


우선순위 큐?
배열을 이용해서 하면 아무래도 원소의 재배치 할대 메모리 낭비가 큼,,! 



큐의 활용 => 버퍼! 


EX) 파이참의 입력 버퍼,,,


------------------------------------------------------

BFS,,, 시작

약간 거리순 탐색?,,, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 방문! 


거리가 가까운 순서대로 줄을 서라,,,!!


BFS는 다중 출발점이 가능! DFS는 안되고,,! 약간 차이!


P.59

<BFS 초기화>
방문표시생성
큐생성
시작점 인큐


큐가 비어있지 않으면 반복! => While 큐 not is엠프티:



while q : 
v <- 디큐

v의 비지티드 배열 체크

v <- v의 인접인 w를 인큐



중복이 발생하면,,, 큐의 사이즈가 더 커야겟네? 딱 버텍스의 수만큼 만드는것이 아니라!



'''

'''

단계를 말로 표현할 수 있어야 해! 



방법2 인큐와 비지티드 표시를 같이 묶어서!! 



'''