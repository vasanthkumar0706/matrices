a = [[1, 2, 3] [4, 5, 6]]

result = [[0, 0] [0, 0] [0, 0]]
for i in range (2):
    for j in range (3):
        result[j][i] = a[i][j]

print("transpose of two matrices:")
for row in result:
    print(row)