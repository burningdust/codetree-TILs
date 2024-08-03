arr1 = []
arr2 = []

for _ in range(3):
    row = list(map(int, input().split()))
    arr1.append(row)
input()
for _ in range(3):
    row = list(map(int, input().split()))
    arr2.append(row)

arr3 = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr3[i][j] = arr1[i][j]*arr2[i][j]

for row in arr3:
    for elem in row:
        print(elem, end=" ")
    print()