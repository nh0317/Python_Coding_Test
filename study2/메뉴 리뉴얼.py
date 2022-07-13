from collections import defaultdict
import itertools


def solution(orders, course):
    answer = []
    sets = [defaultdict(int) for _ in range(max(course) + 1)]

    for order in orders:
        for n in course:
            set_menus = list(itertools.combinations(order, n))
            for menu in set_menus:
                menu = "".join(sorted(list(menu)))
                sets[n][menu] += 1

    for s in sets:
        maxx = max(s.values()) if s else 0
        menus = sorted(s.items(), key=lambda x: -x[1])
        if maxx > 1:
            for menu, cnt in menus:
                if maxx == cnt:
                    answer.append(menu)

    answer.sort()
    return answer