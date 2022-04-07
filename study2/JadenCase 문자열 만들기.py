def solution(s):
    s=s.lower()
    words = s.split(' ')
    for i in range(len(words)):
        if words[i]!='' and words[i][0].isalpha():
            words[i]=words[i][0].upper()+words[i][1:]
    answer = ' '.join(words)
    return answer