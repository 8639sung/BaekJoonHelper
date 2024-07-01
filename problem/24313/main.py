a1, a0 = map(int, input().split(" "))
c = int(input())
n0 = int(input())

answer = 0
if c > a1:
        if n0 >= a0/(c-a1):
                answer = 1
elif c == a1:
        if a0 <= 0:
                answer = 1
else:
        pass

print(answer)