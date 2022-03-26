import heapq


def solution(operations):
    answer = []
    q = []
    for ops in operations:
        if ops.startswith("I"):
            heapq.heappush(q, int(ops[2:]))
        elif ops.startswith("D -1") and q:
            heapq.heappop(q)
        elif ops.startswith("D 1") and q:
            maxx = max(q)
            q.remove(maxx)

    if len(q) >= 2:
        answer.append(max(q))
        answer.append(heapq.heappop(q))
    elif len(q) == 1:
        answer = [q[0], q[0]]
    elif not q:
        answer = [0, 0]

    return answer