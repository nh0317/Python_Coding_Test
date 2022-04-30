import copy

maxx = -10000
N = 0
answer = [-1]


# 어피치와 라이언의 점수를 계산
def cal_score(infos, lions):
    global maxx
    global answer
    pscore, lscore = 0, 0
    for j in range(0, len(infos)):
        if infos[j] >= lions[j] and infos[j] != 0:
            pscore += (10 - j)
        elif infos[j] < lions[j]:
            lscore += (10 - j)

    # 점수 차가 더 클 수 있는 경우
    if maxx < lscore - pscore:
        answer = copy.deepcopy(lions)
        maxx = lscore - pscore

    # 점수 차가 동일한 경우
    # 끝부터 탐색하여 가장 낮은 점수가 더 많은 경우에만 갱신
    elif maxx == lscore - pscore:
        if answer != [-1]:
            for i in range(10, 0, -1):
                if lions[i] < answer[i]:
                    break
                if lions[i] > answer[i]:
                    answer = copy.deepcopy(lions)
                    break
        else:
            answer = copy.deepcopy(lions)


def backtracking(idx, infos, lions, summ):
    global maxx
    global answer
    # 범위를 벗어나는 경우
    if summ > N and idx >= 10:
        return

        # 정답인 경우
    elif summ == N and idx == 10:
        cal_score(infos, lions)

    # 맨 마지막의 값을 채우는 경우 (예시 4)
    elif summ < N and idx == 10 and maxx < 0:
        lions[10] = N - summ
        cal_score(infos, lions)

    # 점수를 얻거나 빼본다.
    elif idx < 10:
        idx += 1
        # 포함 함
        lions[idx] = infos[idx] + 1
        backtracking(idx, infos, lions, summ + infos[idx] + 1)

        # 포함 안 함
        lions[idx] = 0
        backtracking(idx, infos, lions, summ)


def solution(n, infos):
    global N
    global maxx
    global answer
    N = n
    backtracking(-1, infos, [0 for _ in range(len(infos))], 0)

    # 동점이거나 낮은 경우
    if maxx <= 0: return [-1]

    # 이기는 경우
    return answer