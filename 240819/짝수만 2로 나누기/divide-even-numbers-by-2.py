def even_devide(N, arr):
    for i in range(N):
        if arr[i]%2==0:
            arr[i] //= 2


n = int(input())
arr = list(map(int, input().split()))

even_devide(n, arr)

for elem in arr:
    print(elem, end=" ")