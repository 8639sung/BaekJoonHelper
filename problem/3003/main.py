import sys

set = [1, 1, 2, 2, 2, 8]
chess = sys.stdin.readline().split(' ')

answer = ' '.join([str(int(a) - int(b)) for a, b in zip(set, chess)])
print(answer)