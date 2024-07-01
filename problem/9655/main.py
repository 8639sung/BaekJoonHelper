import sys

N = int(sys.stdin.readline())
# print("SK" if N%2==1 else "CY")
sys.stdout.write("SK" if N%2==1 else "CY" + '\n')