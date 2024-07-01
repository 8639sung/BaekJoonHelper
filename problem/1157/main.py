import sys

string = sys.stdin.readline().rstrip()

count = {}
string_list = list(string.upper())
for string in string_list:
        try: count[string] += 1
        except: count[string] = 1

max_count = max(count.values())
answer = [key for key, value in count.items() if value == max_count]

if len(answer) == 1:
        print(answer[0])
else:
        print("?") 

