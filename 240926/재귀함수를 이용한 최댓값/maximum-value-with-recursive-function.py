def maximum(n, arr):
    if n==2:
        if arr[0] < arr[1]:
            return arr[1]
        else:
            return arr[0]

    if maximum(n-1, arr) < arr[n-1]:
        return arr[n-1]
    else:
        return maximum(n-1, arr)


n = int(input())
arr = list(map(int, input().split()))
print(maximum(n, arr))