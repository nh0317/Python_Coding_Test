def check(strs):
    stack = []
    for s in strs:
        if s in '({[':
            stack.append(s)
        elif s in ')}]':
            if not stack:
                return False
            elif s == ')' and stack[-1]=='(':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
    
    if stack:
        return False
    else : return True 
    

def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer