from collections import defaultdict
import heapq

def solution(genres, plays):
    musics = defaultdict(list)
    cnt_genres = defaultdict(int)
    
    for i, genre in enumerate(genres):
        cnt_genres[genre] += plays[i]
        heapq.heappush(musics[genre],[-plays[i],i])
        
    cnt_genres = sorted(cnt_genres.items(), key=lambda x: -x[1])
    
    answer = []
    for genre, cnt in cnt_genres:
        for _ in range(2):
            if musics[genre]:
                play, i = heapq.heappop(musics[genre])
                answer.append(i)
            
    return answer