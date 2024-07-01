from itertools import permutations

N, M = map(int, input().split(" "))

answer = []
for combi in permutations(range(1, N+1), M):
        answer.append(' '.join([str(num) for num in combi]))
[print(i) for i in sorted(answer)]
