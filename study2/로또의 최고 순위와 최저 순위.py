def rank(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    unknown = 0

    for num in lottos:
        if num == 0:
            unknown += 1

    result = set(lottos).intersection(set(win_nums))
    answer.append(rank(len(result) + unknown))
    answer.append(rank(len(result)))

    return answer