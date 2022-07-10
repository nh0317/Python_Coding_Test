def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cameras = [routes[0][1]]
    visited = [False for _ in range(len(routes))]

    for i in range(len(routes)):
        for camera in cameras:
            if routes[i][0] <= camera <= routes[i][1]:
                visited[i] = True

        if not visited[i]:
            cameras.append(routes[i][1])

    answer = len(cameras)
    return answer