#Matrix is a 2 dimensional array or List........

matrix = [

[45, 45, 54, 34,],
[34, 53, 53, 43]

]


#value change.....
matrix[1][3] = 100


#print matrix....
num = matrix[1][3]
print(num)
    

#list print on column using for loop......
for row in matrix:
    for column in row:
        print(column)
        

