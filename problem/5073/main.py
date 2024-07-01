def check_triangle(X, Y, Z):
        if max(X, Y, Z)*2 < X+Y+Z: 
                if X == Y and Y == Z:
                        return "Equilateral"
                elif X == Y or Y == Z or Z == X:
                        return "Isosceles"
                else:
                        return "Scalene"
        else:
                return "Invalid"

while True:    
        X, Y, Z = map(int, input().split())
        if X == 0 and Y == 0 and Z == 0:
                break
        else:
                print(check_triangle(X, Y, Z))