def get_turn(answer, i, n):
    answer.append(i % n + 1) # 탈락한 사람
    answer.append(i // n + 1)

def solution(n, words):
    answer = []
    said = set()
    said.add(words[0])
    for i in range(1, len(words)):
        if (words[i] in said) or (words[i-1][-1] != words[i][0]):
            get_turn(answer, i, n)
            break
        if (words[i] not in said) and (words[i-1][-1] == words[i][0]) :
            said.add(words[i])
    
    return answer if answer else [0,0]