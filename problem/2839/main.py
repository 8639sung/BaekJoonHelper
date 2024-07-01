N = int(input())

answer = N//5
while answer >= 0:
        if ((N-answer*5)%3) == 0:
                answer += (N-answer*5)//3
                break
        answer -= 1
print(answer)