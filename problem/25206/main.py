grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
score = []
credit = 0

while True:
        try:
            S = input()
            if S == '':
                break
            else:
                for G in grade:
                        if S.split(' ')[2] == G:
                                score.append(float(S.split(' ')[1])*grade[G]) 
                                credit += float(S.split(' ')[1])
        except EOFError:
            break

print(sum(score)/credit)