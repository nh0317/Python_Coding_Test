from collections import defaultdict, deque

def travel(start, graph, tickets, route):
    global answer
    if answer:
        return
    
    if not tickets:
        answer = route
        return
    
    for v in graph[start]:
        if [start,v] in tickets:
            tickets.remove([start,v])
            travel(v, graph, tickets, route+[v])
            tickets.append([start,v])
    
def solution(tickets):
    global answer
    answer = []
    visit = set()
    
    graph = defaultdict(list)
    for u, v in tickets:
        graph[u].append(v)
        visit.add((u,v))
    
    for u in graph.keys():
        graph[u] = sorted(graph[u])
        
    travel("ICN",graph,tickets,["ICN"])
    return answer