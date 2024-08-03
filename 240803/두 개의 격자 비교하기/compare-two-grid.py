size = input().split()
n,m = int(size[0]), int(size[1])
arr1 = []
arr2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr1.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    arr2.append(row)

arr3 = [[1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            arr3[i][j] = 0

for row in arr3:
    for elem in row:
        print(elem, end=" ")
    print()