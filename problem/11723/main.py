import sys

S = {i+1:False for i in range(20)}

def add(N):
        global S
        S[N] = True
        return 

def remove(N):
        global S
        S[N] = False
        return

def check(N):
        if S[N]:
                return print(1)
        else:
                return print(0)

def toggle(N):
        if S[N]:
                remove(N)
        else:
                add(N)
        return

def all():
        global S
        S = {i+1:True for i in range(20)}
        return
        
def empty():
        global S
        S = {i+1:False for i in range(20)}
        return

M = int(sys.stdin.readline())
functions = {
        "check": check,
        "add": add,
        "remove": remove,
        "toggle": toggle,
        "all": all,
        "empty": empty
}

for i in range(M):
        temp = sys.stdin.readline().strip().split(" ")
        if len(temp) == 1:
                F = temp[0]
                functions[F]()
        else:
                F, N = temp[0], temp[1]
                functions[F](int(N))