import sys
import itertools
import heapq

input = sys.stdin.readline

word = input().rstrip()
orders = []
not_used = set([i for i in range(len(word))])

for i in range(1,len(word)+1):
    pq = []
    for j in not_used:
        new_word = ""
        for w in sorted(orders + [j]):
            new_word += word[w]
        heapq.heappush(pq, [new_word, j])
    print(pq[0][0])
    orders.append(pq[0][1])
    not_used.remove(pq[0][1])