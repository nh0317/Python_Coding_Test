
def solution(n, m, y, x, queries):
    sy, sx = y, x
    ey, ex = y, x
    for command, dx in reversed(queries):
        if command == 0:
            if sx == 0:
                ex = min(m-1,ex+dx)
            else:
                if sx+dx >= m:
                    return 0

                ex = min(m-1,ex+dx)
                sx = min(m-1,sx+dx)

        elif command == 1:
            if ex == m-1:
                sx = max(0,sx-dx)
            else:
                if ex-dx < 0:
                    return 0
                sx = max(0,sx-dx)
                ex = max(0,ex-dx)

        elif command == 2:
            if sy == 0:
                ey = min(n-1,ey+dx)
            else:
                if sy+dx >= n:
                    return 0
                ey = min(n-1,ey+dx)
                sy = min(n-1,sy+dx)

        elif command == 3:
            if ey == n-1:
                sy = max(0,sy-dx)
            else:
                if ey - dx < 0:
                    return 0        
                sy = max(0,sy-dx)
                ey = max(0,ey-dx)
                
    return (abs(ey-sy) + 1) * (abs(ex-sx) + 1)