import sys

P = int(sys.stdin.readline())
for i in range(P):
        T = list(map(int, sys.stdin.readline().strip().split(" ")))
        answer = 0
        sort = []
        sort.append(T.pop(1))
        while (len(T) > 1):
                temp = T.pop(1)
                for i in range(len(sort)):
                        if temp > sort[i]:
                                sort.insert(i, temp)
                                break
                        else: 
                                answer += 1
                        if i == len(sort)-1:
                                sort.append(temp)
        print(T[0], answer)