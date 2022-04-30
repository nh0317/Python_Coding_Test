def make_first_dic(x, cnt):
    add_110 = '110' * cnt
    idx = x.find('11')
    if idx != -1:
        x = x[:idx] + add_110 + x[idx:]
    else:
        idx = x[::-1].find('0')
        if idx != -1:
            idx = len(x) - idx
            x = x[:idx] + add_110 + x[idx:]
        else:
            idx = x.find('1')
            x = x[:idx] + add_110 + x[idx:]
    return x


def remove110(x, i):
    return x[:i] + x[i + 3:]


def solution(s):
    answer = []
    for x in s:
        stack = []
        cnt = 0
        for w in x:
            if (len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and w == '0'):
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(w)

        word = ''.join(stack)
        word = make_first_dic(word, cnt)

        answer.append(word)
    return answer