arr = list(map(int, input().split()))
min_val = arr[0]
max_val = arr[0]

for n in arr[1:]:
    if n==-999 or n==999:
        break
    elif min_val > n:
        min_val = n
    elif max_val < n:
        max_val = n

print(max_val, min_val)