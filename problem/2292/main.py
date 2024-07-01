import sys

N = int(sys.stdin.readline())

i = 1
while (N > 1): 
        i += 1
        N -= (i-1)*6 
print(i)