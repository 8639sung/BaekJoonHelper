import sys

N = int(sys.stdin.readline())
answer = 0

for _ in range(N):
        string = list(sys.stdin.readline().rstrip())
        unique_string = [string[0]]
        for letter in string:
                if unique_string[-1] != letter:
                        unique_string.append(letter)
        if len(unique_string)==len(set(unique_string)):
                answer += 1

print(answer)