import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

def last_in_order(node):
    global tree
    global last
    if node == -1:
        return
    last_in_order(tree[node][0])
    last = node
    last_in_order(tree[node][1])


def in_order_travel(tree):
    global parents

    stack = [1]
    n = len(tree) - 1
    visited = [False for _ in range(len(tree))]

    path = 0
    while stack:
        u = stack.pop()
        path += 1
        if tree[u][0] != -1 and not visited[tree[u][0]]:
            stack.append(tree[u][0])
        elif tree[u][1] != -1 and not visited[tree[u][1]]:
            stack.append(tree[u][1])
        elif u == last:
            return path -1
        elif parents[u] != -1:
            stack.append(parents[u])

        if (tree[u][0] == -1 and tree[u][1] == -1) or visited[tree[u][0]]:
            visited[u] = True
                # n -= 1

        # if n == 0:
        #     return path - 1
        #
        # check = False
        # for i in range(1, -1, -1):
        #     v = tree[u][i]
        #     if v != -1 and not visited[v]:
        #         stack.append(v)
        #         check = True
        #
        # if not check and parents[u] != -1:
        #     if n > 1 or not visited[parents[u]]:
        #         stack.append(parents[u])

    return path




N = int(input())
tree = [[] for _ in range(N+1)]
parents = [-1 for _ in range(N+1)]

for _ in range(1,N+1):
    i, u, v = map(int, input().split())
    tree[i].extend([u,v])
    if u != -1:
        parents[u] = i
    if v != -1:
        parents[v] = i
        
last = 0
last_in_order(1)
print(in_order_travel(tree))