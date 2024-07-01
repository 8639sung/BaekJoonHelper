import sys

def cantoring(N):
        answer = "-"
        for i in range(N, 0, -1):
                answer = answer + " " * len(answer) + answer
        return answer

while True:
        try:
                N = int(sys.stdin.readline())
                print(cantoring(N))
        except:
                break