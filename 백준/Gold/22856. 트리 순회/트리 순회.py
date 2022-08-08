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
    # print(last)
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
        
        # 문제의 조건 
        # 1. 왼쪽 노드가 있고, 방문하지 않은 경우 
        if tree[u][0] != -1 and not visited[tree[u][0]]:
            stack.append(tree[u][0])
            
        # 2. 오른쪽 노드가 있고 방문하지 않은 경우 
        elif tree[u][1] != -1 and not visited[tree[u][1]]:
            stack.append(tree[u][1])
            
        # 3. 중위 순회와 같은 노드로 이동한 경우 탐색 종료 
        elif u == last:
            return path -1
        
        # 4. 부모 노드로 이동 
        elif parents[u] != -1:
            stack.append(parents[u])
        
        # 중위 순회 시 방문 조건 
        # leaf 노드 이거나 왼쪽 노드를 방문한 경우 
        if (tree[u][0] == -1 and tree[u][1] == -1) or visited[tree[u][0]]:
            visited[u] = True

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
last_in_order(1) # 중위 순회에서 마지막 노드 찾기
print(in_order_travel(tree))