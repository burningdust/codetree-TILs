N = int(input())
arr = list(map(int, input().split()))

while True:
    max_val = arr[0]
    for elem in arr:
        if max_val < elem:
            max_val = elem
    idx = arr.index(max_val)
    print(idx+1, end=" ")
    arr = arr[:idx]
    if idx==0:
        break