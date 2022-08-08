import sys
from collections import Counter

input = sys.stdin.readline

trees = []
while True:
    tree = input().rstrip()
    if tree == '':
        break
    trees.append(tree)

species = Counter(trees)
summ = sum(species.values())
for s in species.keys():
    species[s] = species[s]/summ * 100

species = sorted(species.items(), key=lambda x:x[0])

for s, percent in species:
    print("%s %.4f" %(s,percent))

