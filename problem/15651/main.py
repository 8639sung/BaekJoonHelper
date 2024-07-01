from itertools import product

N, M = map(int, input().split(" "))

answer = product("".join([str(i) for i in range(1, N+1)]), repeat=M)
[print(" ".join(i)) for i in answer]