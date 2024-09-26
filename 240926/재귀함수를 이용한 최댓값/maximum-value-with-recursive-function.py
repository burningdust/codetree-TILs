def maximum(n, arr):
    if n==1:
        return arr[0]
    
    previous = maximum(n-1, arr)
    if arr[n-1] > previous:
        return arr[n-1]
    else:
        return previous


n = int(input())
arr = list(map(int, input().split()))
print(maximum(n, arr))