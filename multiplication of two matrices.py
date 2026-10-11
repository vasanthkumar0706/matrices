a = [[1,2] [3,5]]

b = [[1,3] [4,5]]

result = [[0,0][0,0]]

for i in range(2):
    for j in range(2):
        for k in range (2):
            result[i][j] += a[i][k] * b[k][j]
print("multiplication of two matrices:")
for row in result:
    print(row)