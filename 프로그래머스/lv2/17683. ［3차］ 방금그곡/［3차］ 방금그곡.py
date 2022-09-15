from collections import defaultdict
import re
def convertTime(time):
    h, m =map(int, time.split(":"))
    m += h * 60
    return m

def solution(m, musicinfos):
    answer = []
    musics = defaultdict(list)
    
    for node in "ABCDEFG":
        m = re.sub(node+"#", node.lower(),m)
    
    for i,info in enumerate(musicinfos):
        start, end, title, melody = info.split(",")
        
        
        for node in "ABCDEFG":
            melody = re.sub(node+"#", node.lower(),melody)
            
        start = convertTime(start)
        end = convertTime(end)
        playTime = end - start
        
        l = len(melody)
        mm = playTime // l
        r = playTime % l
            
        melody = melody * mm + melody[:r]
        musics[melody].append([title, playTime,i])
    
    for melody in musics.keys():
        if re.fullmatch(".*"+m+".*", melody):
        # if melody.find(m) != -1 and melody.find(m+'#') == -1:
            for music in musics[melody]:
                answer.append(music)
    
    
    if answer:
        answer.sort(key=lambda x: (-x[1],x[2]))
        
    else: 
        return "(None)"
    
    return answer[0][0]