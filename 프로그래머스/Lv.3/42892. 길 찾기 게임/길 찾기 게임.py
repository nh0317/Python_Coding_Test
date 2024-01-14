from collections import deque
import sys
sys.setrecursionlimit(10**6)

def find_parent(x, root, graph, nodeinfo):
    q = deque()
    q.append(root)
    while q:
        root = q.popleft()
        # print(root)

        if nodeinfo[root - 1][0] < x and graph[root][1]:
            q.append(graph[root][1])

        elif nodeinfo[root - 1][0] > x and graph[root][0]:
            q.append(graph[root][0])
            
        else:
            return root

def prefix(root, graph, answer):
    answer[0].append(root)
    if graph[root][0]:
        prefix(graph[root][0], graph, answer)
    if graph[root][1]:
        prefix(graph[root][1], graph, answer)

def postfix(root, graph, answer):
    if graph[root][0]:
        postfix(graph[root][0], graph, answer)
    if graph[root][1]:
        postfix(graph[root][1], graph, answer)
    answer[1].append(root)

def solution(nodeinfo):
    nodes = [[point[0], point[1], i + 1] for i, point in enumerate(nodeinfo)]
    nodes = sorted(nodes, key=lambda x: (-x[1], x[0]))

    graph = [[0,0] for _ in range(len(nodeinfo) + 1)]
    parent = nodes[0][2]
    cury = nodes[0][1]
    root = nodes.pop(0)[2]
    left = False
    right = False

    for i, n in enumerate(nodes):
        x, y, node = n

        parent = find_parent(x, root, graph, nodeinfo)
        if (left and right) or (left and nodeinfo[parent - 1][0] >= x) or (right and nodeinfo[parent - 1][0] < x):
            parent = find_parent(x, root, graph, nodeinfo)
            left = False
            right = False
        # print(parent, node)

        if nodeinfo[parent - 1][0] < x and not right:
            graph[parent][1] = node
            right = True
        elif nodeinfo[parent - 1][0] > x and not left:
            graph[parent][0] = node
            left = True
        cury = y
    # for i,u in enumerate(graph):
    #     print(i,u)
    answer = [[],[]]
    prefix(root, graph, answer)
    postfix(root, graph, answer)
    return answer
