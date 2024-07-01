import sys

string = list(sys.stdin.readline().rstrip())
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = len(string)

for i in range(0, len(string)-1):
        for word in croatia:
                if string[i]+string[i+1] == word:
                        answer -= 1
                elif i != 0 and string[i-1]+string[i]+string[i+1] == word:
                        answer -= 1     
        
print(answer)