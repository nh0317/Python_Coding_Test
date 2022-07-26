import sys
from collections import defaultdict, deque

musics = defaultdict(int)

def move(music):
    if music == 'FF' or music=='SF':
        return ['FF','FS']
    elif music == 'SS' or music == 'FS':
        return ['SS','SF']

def bfs(start):
    global musics
    ff, fs, sf, ss = musics.values()
    summ = sum(musics.values())

    visited = defaultdict(list)
    visited['FF'] = [False for _ in range(summ+1)]
    visited['FS'] = [False for _ in range(summ+1)]
    visited['SF'] = [False for _ in range(summ+1)]
    visited['SS'] = [False for _ in range(summ+1)]
    maxx = 1
    visited[start][1] = True
    if start == 'FF':
        ff -= 1
    elif start == 'FS':
        fs -= 1
    elif start == 'SF':
        sf -= 1
    else: ss -= 1
    q = deque([[start, ff, fs, sf, ss, 1]])

    while q:
        u, ff, fs, sf, ss, cnt = q.popleft()
        for v in move(u):
            if cnt +1 <= summ and not visited[v][cnt+1]:
                if v == 'FF' and ff > 0:
                    q.append([v, ff-1, fs, sf, ss, cnt+1])
                    visited[v][cnt+1] = True
                elif v == 'FS' and fs > 0:
                    q.append([v, ff, fs-1, sf, ss, cnt+1])
                    visited[v][cnt+1] = True
                elif v == 'SF' and sf > 0:
                    q.append([v, ff, fs, sf-1, ss, cnt+1])
                    visited[v][cnt+1] = True
                elif v == 'SS' and ss > 0:
                    q.append([v, ff, fs, sf, ss-1, cnt+1])
                    visited[v][cnt+1] = True
                else:
                    maxx = max(maxx, cnt)
            else:
                maxx = max(maxx, cnt)

    return maxx



input = sys.stdin.readline
ff, fs, sf, ss = map(int, input().split())
musics['FF'] = ff
musics['FS'] = fs
musics['SF'] = sf
musics['SS'] = ss
maxx = 0

if ff >0:
    maxx = max(maxx, bfs('FF'))
if fs > 0:
    maxx = max(maxx, bfs('FS'))
if ff == 0 and fs == 0:
    if sf > 0:
        maxx = max(maxx, bfs('SF'))
    if ss > 0:
        maxx = max(maxx, bfs('SS'))

print(maxx)

