import sys, re, itertools

input = sys.stdin.readline

def make_joy_word(words,word,cnt):
    global blank
    global answer
    global blank_idx
    global is_l

    if cnt == blank:
        if check(blank_idx[cnt-1], word) :
            # l이 원래 단어에 있는 경우
            if is_l:
                # 5^(모음의 수) + 21^(자음의 수)
                answer += int(5 ** words[0] * 21 ** words[1])

            # l이 없는 경우
            else:
                if words[1]>0:
                    for i in range(1,words[1]):
                        #l의 자리를 뽑는다.
                        place = len(list(itertools.combinations([i for i in range(words[1])],i)))

                        # 5 ^ (모음의 수) * 20(l제외 자음의 수)^(l이 아난 자음의 수) * l의 자리
                        answer += int(5 ** words[0] * 20 ** (words[1]-i) * place)
                    # 전부 l인 경우
                    answer += int(5 ** words[0])

    else:
        if cnt == 0 or check(blank_idx[cnt-1], word):
            for i in range(0,2):
                new_word = word[:blank_idx[cnt]]+chr(i+ord('a'))+word[blank_idx[cnt]+1:]
                words[i] += 1 # 모음/자음의 수
                make_joy_word(words,new_word,cnt+1)
                words[i] -= 1

def check(blank_idx, word):
    # 현재 채운 알파벳 앞
    start = max(0, blank_idx - 2)
    if check_range(start, blank_idx, word):
        return False

    # 현재 채운 알파벳 좌우
    start = max(0, blank_idx-1)
    end = min(len(word)-1, blank_idx+1)
    if check_range(start, end, word):
        return False

    # 현재 채운 알파벳 뒤
    end = min(len(word)-1, blank_idx+2)
    if check_range(blank_idx, end, word):
        return False
    return True


def check_range(start, end, word):
    cnt1 = 0
    cnt2 = 0
    for i in range(start, end+1):
        if word[i] == 'a':
            cnt1+=1
        elif word[i] != '_': cnt2+=1
    if cnt1 == 3 or cnt2==3:
        return True
    else:
        return False


blank_word = str(input()[:-1]).lower()
blank = blank_word.count('_')
blank_idx = []
is_l = False

if 'l' in blank_word: is_l = True
blank_word = re.sub('[aeiou]','a',blank_word) # 모음 -> a
blank_word = re.sub('[^a_]','b', blank_word) # 자음 -> b

for i,w in enumerate(blank_word):
    if w == '_':
        blank_idx.append(i)

answer = 0
make_joy_word([0,0],blank_word,0)
print(answer)