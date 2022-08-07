import sys
from collections import defaultdict

input = sys.stdin.readline

def find_parents(k):
    global parents
    for children in parents.keys():
        if k in children:
            # print(children)
            return parents[children]
    return k

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    tree = [[] for _ in range(n+1)]
    seqs = list(map(int, input().split()))
    tree[0].append(seqs[0])
    parents = defaultdict(int)
    j = 1
    children = 0
    for i in range(1, len(seqs)-1):
        if seqs[i] + 1 == seqs[i+1]:
            tree[j].append(seqs[i])
        else:
            tree[j].append(seqs[i])
            j += 1
    if j < n:
        tree[j].extend(seqs[-1:])
    # print(tree)
    siblings = [[] for _ in range(n+2)]
    siblings[0] = tree[0]

    j = 0
    for i in range(len(tree)):
        if i < len(siblings):
            for s in range(len(siblings[i])):
                if j + s + 1 < len(tree) and i+1 < len(siblings):
                    siblings[i+1].extend(tree[j+s+1])
                    # print(tree[j+s+1],siblings[i][s])
                    parents[tuple(tree[j+s+1])] = siblings[i][s]
                    # print(i+1, tree[j+s+1], tree[i][s])
        j+=len(siblings[i])
        if not tree[i]:
            break
    # print(siblings)
    # print(parents)
    generations = []
    grand = 0
    parent = 0
    for s in siblings:
        if k in s:
            parent = find_parents(k)
            grand = find_parents(parent)
            generations.extend(s)

    cnt_siblings = 0
    for g in generations:
        if g != k:
            parent2 = find_parents(g)
            grand2 = find_parents(parent2)
            # print(g, parent2, grand2)
            if parent2 != parent and grand2 == grand:
                cnt_siblings += 1

    # for t in tree:
    #     if k in t:
    #         cnt_siblings = len(t)
    print(cnt_siblings)



