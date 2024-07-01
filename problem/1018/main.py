def numberize(string):
        num = []
        for i in string:
                if i == 'W':
                        num.append(1)
                else:
                        num.append(0)
        return num

def compare_chessboards(board1, board2, x, y):
        diff = 0
        for i in range(8):
                for j in range(8):
                        if board1[i][j] != board2[x+i][y+j]:
                                diff += 1
        return diff

checkboard = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        ]

N, M = map(int, input().split(" "))

chessboard = []
for _ in range(N):
        chessboard.append(numberize(input()))

answer = compare_chessboards(checkboard, chessboard, 0, 0)
for i in range(N-7):
        for j in range(M-7):
                sum = compare_chessboards(checkboard, chessboard, i, j)
                sum = min((64 - sum), sum)
                if answer > sum:
                        answer = sum
print(answer)