def get_set(str1):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    set1 = []
    str1 = str1.lower()
    for i in range(len(str1) - 1):
        if str1[i] in alpha and str1[i + 1] in alpha:
            set1.append(str1[i:i + 2])
    return set1


def duplicate(list1, list2):
    len_union = 0
    len_inter = 0
    inter = set(list1).intersection(set(list2))
    union = set(list1).union(set(list2))
    for s in union:
        num1, num2 = 0, 0
        for l in list1:
            if s == l:
                num1 += 1
        for l in list2:
            if s == l:
                num2 += 1
        len_union += max(num1, num2)
        len_inter += min(num1, num2)

    return len_inter, len_union


def solution(str1, str2):
    answer = 0
    set1 = get_set(str1)
    set2 = get_set(str2)
    len_inter, len_union = duplicate(set1, set2)

    if (len_union == 0):
        answer = 65536
    else:
        answer = int(len_inter / len_union * 65536)
    return answer

# 56:67.10
# 질문하기에서 반례 찾아 봄