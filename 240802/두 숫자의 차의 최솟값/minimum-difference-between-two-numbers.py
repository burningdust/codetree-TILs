n = int(input())
arr = list(map(int, input().split()))

min_diff = arr[n-1] - arr[0]

for i in range(n-1):
    if arr[i+1] - arr[i] < min_diff:
        min_diff = arr[i+1] - arr[i]

print(min_diff)