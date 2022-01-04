'''


요세푸스 문제

원형 큐?

구현하면 될거 같은데?!

원형 큐 구현하는거 공부하고 풀어보자!


deque에 있는 roatae 함수를 사용하면 쉬을꺼 같기도,,



'''

# def isEmpty():
#     return front == rear
#
# def isFull():
#     return (rear+1) % len(lst) == front
#
#
# def enQueue(item):
#     global rear
#     if isFull():
#         print("꽉참")
#     else:
#         rear = (rear+1) % len(lst)
#         lst[rear] = item
#
# def deQueue():
#     global front
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         front = (front+1)%len(lst)
#         return lst[front]



N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

ans = []

delete_idx = 0

#아 N이 고정이면 안된다!

for _ in range(N):

    delete_idx += K-1

    if delete_idx > len(lst) - 1 :
        delete_idx = delete_idx % len(lst)

    ans.append(str(lst.pop(delete_idx))) # 아 출력을 위해서 여기에

#아 이거 출력이 어렵다,,,
print("<",", ".join(ans)[:],">", sep='')









