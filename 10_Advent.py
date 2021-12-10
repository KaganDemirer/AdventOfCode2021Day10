with open("10_Advent.txt") as input_file:
    read_lines = input_file.readlines()

matrix = []
wrong = []
added = []
tempfix_list = []
fixed_list = []
points = 0

def check_and_fix(old, y, x):
    if x == len(matrix[y]):
        if matrix[old[0]][old[1]] == "(":
            matrix[y].append(")")
            tempfix_list.append(")")
        elif matrix[old[0]][old[1]] == "[":
            matrix[y].append("]")
            tempfix_list.append("]")
        elif matrix[old[0]][old[1]] == "{":
            matrix[y].append("}")
            tempfix_list.append("}")
        elif matrix[old[0]][old[1]] == "<":
            matrix[y].append(">")
            tempfix_list.append(">")
    if matrix[y][x] == "{" or matrix[y][x] == "(" or matrix[y][x] == "<" or matrix[y][x] == "[":
        xn = False, y, x
        old = y, x-1
        while True:
            if xn[0] == True:
                break
            else:
                xn = check_and_fix([old[0],old[1]+1], xn[1], xn[2]+1)
            if xn == "Syntax Error":
                return "Syntax Error"
        return False, xn[1], xn[2]
    elif (matrix[old[0]][old[1]] == "{" and matrix[y][x] == "}") or (matrix[old[0]][old[1]] == "(" and matrix[y][x] == ")") or (matrix[old[0]][old[1]] == "<" and matrix[y][x] == ">") or (matrix[old[0]][old[1]] == "[" and matrix[y][x] == "]"):
        # print("return", y, x, old)
        return True, y, x
    else:
        # print("Syntax Error: ", matrix[y][x], y, x, old)
        wrong.append([y,x])
        return "Syntax Error"

for x in read_lines:
    tm = []
    for l in x[:-1]:
        tm.append(l)
    matrix.append(tm)

for x in range(len(read_lines)):
    check_and_fix([0,0],x,0)
    tscore = 0
    tstring = "".join(str(x) for x in tempfix_list)
    for s in tstring:
        if s == ")":
            tscore = tscore * 5 + 1
        elif s == "]":
            tscore = tscore * 5 + 2
        elif s == "}":
            tscore = tscore * 5 + 3
        elif s == ">":
            tscore = tscore * 5 + 4
    if tscore != 0:
        fixed_list.append(tscore)
    added.append([tstring, x])
    tempfix_list.clear()

for x in wrong:
    if matrix[x[0]][x[1]] == ")":
        points+=3
    elif matrix[x[0]][x[1]] == "]":
        points+=57
    elif matrix[x[0]][x[1]] == "}":
        points+=1197
    elif matrix[x[0]][x[1]] == ">":
        points+=25137

print("Syntax error on: " ,wrong)
print("Points for Syntax Error: ", points)
print()
fixed_list.sort()
print("Points for fixing: ", fixed_list)
print("The middle score is: " , fixed_list[(len(fixed_list)-1)//2])
