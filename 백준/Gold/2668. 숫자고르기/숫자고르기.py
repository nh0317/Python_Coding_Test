import sys

input = sys.stdin.readline

def dfs(start):
    global visited

    q = [start]
    picked = [start]
    visited[start] = True

    is_cycle = False

    while q:
        u = q.pop()
        v = arr[u]

        if not visited[v]:
            q.append(v)
            visited[v] = True
            picked.append(v)

        elif picked and arr[v] in picked:
            picked = picked[picked.index(v):]
            is_cycle = True
            
    if is_cycle:
        return set(picked)
    else : return set()


N = int(input().rstrip())
arr = [0 for _ in range(N+1)]

for i in range(1,N+1):
    arr[i] = int(input().rstrip())

maxx = 0
max_idx = set()

visited = [False for _ in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        max_idx = max_idx.union(dfs(i))

print(len(max_idx))
max_idx = sorted(max_idx)
for i in max_idx:
    print(i)