size = input().split()
n,m = int(size[0]), int(size[1])
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for order in range(n+m-1):
    for i in range(order+1):
        if i>=n or order-i>=m:
            continue
        arr[i][order-i] = num
        num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()