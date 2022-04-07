from collections import Counter

def solution(a):
    answer = -1
    set_n = Counter(a)
    for s in set_n.keys():
        i = 0
        cnt = 0
        if (answer > set_n[s] * 2):
            continue

        while i < len(a):
            if s in a[i:i + 2] and len(a[i:i + 2]) == 2 and a[i] != a[i + 1]:
                i += 2
                cnt += 1
            else:
                i += 1
        answer = max(cnt * 2, answer)
    if answer == -1:
        return 0
    else:
        return answer