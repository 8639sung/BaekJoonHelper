import sys

N = int(sys.stdin.readline())
# star = [" " for i in range(2*N-1)]

# for i in range(2*N-1):
#         if i < N:
#                 star[N-1-i] = "*"
#                 star[N-1+i] = "*"
#                 print(''.join(star))
#         else:
#                 star[i-N] = " "
#                 star[-i+N-1] = " "
#                 print(''.join(star))

for i in range(1, N):
        print(" "*(N-i)+"*"*(2*i-1))
for i in range(N, 0, -1):
        print(" "*(N-i)+"*"*(2*i-1))