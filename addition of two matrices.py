A = [[1, 2] [3, 4]]

B = [[5, 7] [8, 9]]

result = [[0, 0] [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]
print("addition of two matrices :")
for row in result:
    print(row)
