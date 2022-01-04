'''


트리 순회



특이한 입력 -> 이진 트리용으로 받아보자!

흠흠,, 딕셔너리 쓰면 훨씬 편하구나,,!!

파이썬의 장점인 딕셔너리를 적극적으로 사용하자!

'''


#
# test = []
#
#
# for i in  range(1, 3):
#
#     left, right = input().split()
#
#     test.append([left, right])



#전위 순회


def preorder(root): #루트 -> 레프트 -> 라이트

    if root != ".":
        print(root, end="") #루트
        preorder(tree[root][0])  #왼
        preorder(tree[root][1])  #오



#중위 순회
def inorder(root):#레프트 -> 루트 -> 라이트


    if root != ".":

        inorder(tree[root][0])  #왼
        print(root, end="")  # 루트
        inorder(tree[root][1])  #오


#후위 순회
def postorder(root): #레프트 -> 라이트 -> 루트

    if root != ".":

        postorder(tree[root][0])  #왼
        postorder(tree[root][1])  # dh
        print(root, end="")  # 루트


N = int(input())

#A == 1 이라 생각
tree = {}

for i in range(N):

    root, left, right  = input().split()
    tree[root] = [left, right]



#"A에서 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')




