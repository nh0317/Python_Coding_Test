def move(m, k, i):
    global table
    for _ in range(m):
        k = table[k][i]
    return k


def solution(n, k, cmd):
    global table
    table = [[] for _ in range(n)]
    for i in range(n):
        table[i].extend([i - 1, i + 1])

    deleted = []
    for c in cmd:
        if c.startswith("D"):
            d, m = c.split()
            m = int(m)
            k = move(m, k, 1)

        elif c.startswith("U"):
            d, m = c.split()
            m = int(m)
            k = move(m, k, 0)

        elif c == "C":
            deleted.append([k]+table[k])
            cur = k

            if table[k][1] < n:
                table[table[k][1]][0] = table[k][0]
                
            if table[k][0] >= 0:
                table[table[k][0]][1] = table[k][1]

            if table[k][1] == n:
                k = table[k][0]
            else:
                k = table[k][1]

            table[cur] = ['null', 'null']


        elif c == "Z":
            m, pre, post = deleted.pop()
            table[m] = [pre, post]
            if pre >= 0 :
                table[pre][1] = m
            if post < n:
                table[post][0] = m

    answer = ['X'] * n
    for i in range(len(table)):
        if table[i][1] != 'null' and table[i][0] != 'null':
            j = table[i][1]
            answer[i] = 'O'
            while j < n and table[j][1] != 'null':
                answer[j] = 'O'
                j = table[j][1]
            break
            
    return ''.join(answer)