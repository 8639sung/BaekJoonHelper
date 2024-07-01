N = int(input())

answer = 0
for i in range(9*len(str(N)), 0, -1):
        n = N - i
        sum = n
        while n>0:
                sum += n%10
                n //= 10
        if N == sum:
                answer = N - i
                break
print(answer)