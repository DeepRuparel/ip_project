row,column=map(int,input().split(" "))
list_digit=[]
matrix=[]
for r in range(row):
    row_numbers=list(map(int,input().split()))
    matrix.append(row_numbers)
for r in range(0,row):
    for c in range(0,column):
        if(c<column-3):
            if(matrix[r][c]==matrix[r][c+1]==matrix[r][c+2]==matrix[r][c+3]):
                list_digit.append(matrix[r][c])
        if(r<row-3):
            if(matrix[r][c]==matrix[r+1][c]==matrix[r+2][c]==matrix[r+3][c]):
                list_digit.append(matrix[r][c])
        if(r>=3 and c<column-3):
            if(matrix[r][c]==matrix[r-1][c+1]==matrix[r-2][c+2]==matrix[r-3][c+3]):
                list_digit.append(matrix[r][c])
        if(r>=3 and c>=3):
            if(matrix[r][c]==matrix[r-1][c-1]==matrix[r-2][c-2]==matrix[r-3][c-3]):
                list_digit.append(matrix[r][c])
if(len(list_digit)==0):
    print("-1")
else:
    print(min(list_digit))
