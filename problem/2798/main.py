from itertools import combinations

N, M = map(int, input().split(" "))
CARD = list(map(int, input().split(" ")))

answer = 0
for combi in combinations(CARD, 3):
        if answer <= sum(combi) and sum(combi) <= M:
                answer = sum(combi)
print(answer)