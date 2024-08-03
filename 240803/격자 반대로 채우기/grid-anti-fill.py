n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
num = 1

for i in range(n):
    if i%2==0:
        for j in range(n):
            arr[n-j-1][n-i-1] = num
            num += 1
    else:
        for j in range(n):
            arr[j][n-i-1] = num
            num+= 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()