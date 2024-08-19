def abs_list(n, arr):
    for i in range(n):
        if arr[i]<0:
            arr[i] = -arr[i]


N = int(input())
arr = list(map(int, input().split()))
abs_list(N, arr)

for elem in arr:
    print(elem, end=" ")