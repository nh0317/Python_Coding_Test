def addSheepAndWolf(info,u,sheep,wolf):
    if info[u] == 0:
        sheep += 1
    if info[u] == 1:
        wolf += 1
    return sheep, wolf

def subSheepAndWolf(info,u,sheep,wolf):
    if info[u] == 0:
        sheep -= 1
    if info[u] == 1:
        wolf -= 1
    return sheep, wolf

def cntSheepAndWolf(mst,info):
    sheep = 0
    wolf = 0
    for m in mst:
        if info[m]==0:
            sheep +=1
        elif info[m]==1:
            wolf += 1
    return sheep, wolf

def dfs(u, info, graph,visited,mst):
    visited[u] = True
    global maxx
    vnear = []
    for m in mst:
        for w,uu in graph[m]:
            if uu not in vnear and uu not in mst:
                vnear.append(uu)
    sheep,wolf = cntSheepAndWolf(mst,info)
    if sheep > wolf:
        maxx = max(maxx, sheep)

    for nn in vnear:
        if nn not in mst:
            sheep, wolf = addSheepAndWolf(info, nn, sheep, wolf)
            mst.append(nn)
            if sheep > wolf:
                dfs(nn,info,graph,visited,mst)
            mst.remove(nn)
            sheep, wolf = subSheepAndWolf(info, nn, sheep, wolf)

    return maxx

maxx = -1
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for u, v in edges:
        graph[u].append((info[v], v))

    visited = [False for _ in range(len(info))]
    answer = dfs(0,info, graph,visited,[0])

    return answer