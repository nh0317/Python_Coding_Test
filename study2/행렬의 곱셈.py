# import numpy as np
def solution(arr1, arr2):
    answer = []
    # arr1 = np.array(arr1)
    # arr2 = np.array(arr2)
    # answer = np.dot(arr1, arr2).tolist()

    for y1 in range(len(arr1)):
        row = []
        for x1 in range(len(arr2[0])):
            summ = 0
            for x2 in range(len(arr1[0])):
                summ += arr1[y1][x2] * arr2[x2][x1]
            row.append(summ)
        answer.append(row)

    return answer