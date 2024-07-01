N = int(input())

fibonacci = [0, 1]
while(N>=2):
        fibonacci.append(fibonacci[-2]+fibonacci[-1])
        N -= 1
print(fibonacci[-1])