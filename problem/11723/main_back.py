import sys

S = []
ALL = [i+1 for i in range(20)]

def add(N):
        if _check(N) is False:
                S.append(N)
        return

def remove(N):
        if _check(N):
                S.remove(N)
        return

def _check(N):
        if N in S:
                return True
        else:
                return False

def check(N):
        if N in S:
                return print(1)
        else:
                return print(0)

def toggle(N):
        if _check(N):
                remove(N)
        else:
                add(N)
        return

def all():
        global S
        S = ALL
        return
        
def empty():
        global S
        S = []
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
        F = sys.stdin.readline().rstrip()
        try:
                F, N = map(str, F.split(" "))
                functions[F](int(N))
        except:
                functions[F]()