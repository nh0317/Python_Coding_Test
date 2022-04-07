def solution(triangle):
    answer = 0
    for j in range(len(triangle[1])):
        triangle[0].append(triangle[0][0])

    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j], triangle[i][j] + triangle[i - 1][j + 1])

        triangle[i].insert(0, triangle[i][0])
        triangle[i].insert(len(triangle[i]) - 1, triangle[i][len(triangle[i]) - 1])

    answer = max(triangle[len(triangle) - 1])
    return answer