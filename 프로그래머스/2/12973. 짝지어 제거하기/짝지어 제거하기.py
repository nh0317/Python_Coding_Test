from collections import deque

def remove_pair(s):
    if not s:
        return ''
    stack1 = deque()
    stack2 = deque(list(s))
    stack1.appendleft(stack2.popleft())
    
    while stack2:
        ss = stack2.popleft()
        if stack1 and ss == stack1[-1]:
            stack1.pop()
            continue
        stack1.append(ss)
    return ''.join(stack1)

def solution(s):
    answer = 1
    next_s = s[:]
    cnt = 0
    
    while True:
        cnt += 1
        next_s = remove_pair(s)
        if next_s == s or not s:
            break
        s = next_s[:]

    return answer if s == '' else 0