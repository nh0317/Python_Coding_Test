import itertools

def solution(relation):
    cnt = 0
    keys = [x for x in range(len(relation[0]))]
    answer = []
    for i in range(len(relation[0])+1):
        candidates = set(itertools.combinations(keys, i))
        for candidate in candidates:
            sets = set()
            for row in relation:
                r = []
                for c in candidate:
                    r.append(row[c])
                sets.add(tuple(r))
            if len(sets) == len(relation):
                for key in answer:
                    if len(key.union((candidate))) == len(candidate):
                        break
                else:
                    answer.append(set(candidate))
                    # cnt += 1
    # print(answer)
    return len(answer)