from collections import defaultdict, deque
import itertools

cnt = 0
find_answer = False

def next_word(word):
    if word == 'A' : return 'E'
    if word == 'E' : return 'I'
    if word == 'I' : return 'O'
    if word == 'O' : return 'U'
    if word == 'U' : return 'A'

def dictionary(cur, word, visited):
    global cnt 
    global find_answer
    
    if find_answer:
        return
    
    visited.add(cur)
    cnt += 1
    if cur == word:
        find_answer = True
        return 
    
    
    nextt = next_word(cur[-1])
    if len(cur) < 5:
        if cur + 'A' not in visited:
            dictionary(cur + 'A', word, visited)
        if cur + cur[-1] not in visited:
            dictionary(cur + cur[-1], word, visited)
    
    if cur[:-1] + 'A' not in visited:
        dictionary(cur[:-1] + 'A', word, visited)
    
    if cur[:-1] + nextt not in visited:
        dictionary(cur[:-1] + nextt, word, visited)
    

def solution(word):
    global cnt
    visited = set()
    
    dictionary('A', word, visited)
    return cnt