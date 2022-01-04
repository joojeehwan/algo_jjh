



#재귀 : 현재 => 다음 으로 가자!

def recursion(node, ancestors, genertaions):

    
    if node in tree: #자식이 있으면 자식으로 타고 들어가라
        for i , child in enumerate(tree[node], start=1):
            recursion(child, ancestors+ [node], genertaions + [i])

    else:
        #자식이 없다? 마지막 노드이니 한줄을 전부 출력
        ancestors += [node]
        rtn = f"[{str(ancestors[0]).zfill(3)}]"if not printed else "   "

        for i, ancestor in enumerate(ancestors[1:], start =1 ):
            if ancestor in printed: #내가 출력을 했었던 노드인가?!
                rtn += "    |        "
            else:
                sibling_count = len(tree[ancestors[i-1]])
                sibling_ranking = genertaions[i]
                number = str(ancestor).zfill(3)


                if sibling_count == 1:
                    rtn += f" ----- [{number}]"


                elif sibling_ranking == 1:
                    rtn += f" --+-- [{number}]"

                elif sibling_count == sibling_ranking:
                    rtn += f"   L-- [{number}]"

                else:
                    rtn += f"   +-- [{number}]"

                printed.add(ancestor)

        print(rtn)

#딕셔너리,,,!
tree = {}

edges = list(map(int, input().split()))
for i in range(0, len(edges)-1, 2):

    tree[edges[i]] = tree.get(edges[i],[]) + [edges[i + 1]]


printed = set()
recursion(edges[0],[], [1])



