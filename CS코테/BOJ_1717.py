import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def find_parent(sets, u):
    # while sets[u] != u:
    #     u = sets[u]
    # return u

    # 경로 압축 -> 트리의 높이를 낮춰서 탐색 시간 최적화
    # https://eun-jeong.tistory.com/15
    if sets[u] != u:
        sets[u] = find_parent(sets, sets[u])
    print(sets)
    return sets[u]

def union_set(sets, u, v):
    u = find_parent(sets,u)
    v = find_parent(sets,v)
    if u < v:
        sets[v] = u
    else: sets[u] = v

def is_in(sets, u, v):
    if find_parent(sets,u) == find_parent(sets,v):
        return "YES"
    else: return "NO"

n, m = map(int, input().split())
sets = [x for x in range(n+1)]

for _ in range(m):
    op, u, v = map(int, input().split())
    if op == 1:
        print(is_in(sets, u, v))
    elif op == 0:
        union_set(sets, u, v)
