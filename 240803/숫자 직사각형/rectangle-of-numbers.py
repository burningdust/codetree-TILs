size = input().split()
n,m = int(size[0]), int(size[1])

arr = []
num = 1
for _ in range(n):
    row = []
    for _ in range(m):
        row.append(num)
        num += 1
    arr.append(row)

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()