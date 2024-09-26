def maximum(n, arr):
    if n==1:
        return arr[0]
    
    if arr[n-1] > maximum(n-1, arr):
        return arr[n-1]
    else:
        return maximum(n-1, arr)


n = int(input())
arr = list(map(int, input().split()))
print(maximum(n, arr))