import sys
from collections import defaultdict, deque

input = sys.stdin.readline

T = int(input())

def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u],parent)
    return parent[u]

def union(u,v,parent, children):
    u = find(u, parent)
    v = find(v, parent)
    if u != v:
        parent[v] = u
        children[u] += children[v]
for _ in range(T):
    F = int(input())
    friend_dict = defaultdict(str)
    children = defaultdict(lambda :1)

    for _ in range(F):
        friend1, friend2 = input().split()
        if friend2 not in friend_dict.keys():
            friend_dict[friend2] = friend2
        if friend1 not in friend_dict.keys():
            friend_dict[friend1] = friend1

        union(friend1, friend2, friend_dict, children)
        print(children[find(friend1, friend_dict)])
