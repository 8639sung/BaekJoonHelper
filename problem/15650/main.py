from itertools import combinations

N, M = map(int, input().split(" "))

answer = []
for combi in combinations(range(1, N+1), M):
        answer.append(' '.join([str(num) for num in combi]))
[print(i) for i in sorted(answer)]